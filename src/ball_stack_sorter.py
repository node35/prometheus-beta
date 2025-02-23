from typing import List, Dict

class BallStackSorter:
    def __init__(self, stacks: Dict[str, List[str]]):
        """
        Initialize the ball stack sorter with three stacks of colored balls.
        
        :param stacks: Dictionary with stack names as keys and lists of ball colors as values
        """
        self.stacks = stacks
        self.total_balls = sum(len(stack) for stack in stacks.values())
        
        # Validate initial conditions
        if len(stacks) != 3:
            raise ValueError("Exactly 3 stacks are required")
        if self.total_balls % 3 != 0:
            raise ValueError("Total number of balls must be divisible by 3")
        
        # Expected number of balls in each stack after sorting
        self.target_stack_size = self.total_balls // 3

    def is_sorted(self) -> bool:
        """
        Check if the stacks are sorted (each stack has an equal number of balls 
        and contains only one color).
        
        :return: True if sorted, False otherwise
        """
        # Check if all stacks have the same number of balls
        if any(len(stack) != self.target_stack_size for stack in self.stacks.values()):
            return False
        
        # Check if each stack contains only one color
        for stack in self.stacks.values():
            if len(set(stack)) > 1:
                return False
        
        return True

    def move_ball(self, from_stack: str, to_stack: str) -> None:
        """
        Move a single ball from one stack to another.
        
        :param from_stack: Name of the source stack
        :param to_stack: Name of the destination stack
        """
        if not self.stacks[from_stack]:
            raise ValueError(f"Cannot move ball from empty stack: {from_stack}")
        
        # Remove ball from source stack and add to destination stack
        ball = self.stacks[from_stack].pop(0)
        self.stacks[to_stack].append(ball)

    def sort_stacks(self) -> List[Dict[str, List[str]]]:
        """
        Sort the stacks using minimal moves while maintaining equal ball count.
        
        :return: List of intermediate stack states during sorting
        """
        # Track intermediate states for visualization/debugging
        states = [dict(self.stacks)]
        
        # If already sorted, return immediately
        if self.is_sorted():
            return states
        
        # Sorting strategy:
        # 1. Count colors in each stack
        # 2. Move balls to create color-pure stacks
        stack_names = list(self.stacks.keys())
        
        while not self.is_sorted():
            # Find stacks with multiple colors
            multi_color_stacks = [
                name for name in stack_names 
                if len(set(self.stacks[name])) > 1
            ]
            
            if not multi_color_stacks:
                # If no multi-color stacks but not sorted, 
                # find appropriate stacks to move between
                for i in range(len(stack_names)):
                    for j in range(i+1, len(stack_names)):
                        self.move_ball(stack_names[i], stack_names[j])
                        states.append(dict(self.stacks))
                        break
                    break
            else:
                # Move balls from multi-color stacks
                for stack_name in multi_color_stacks:
                    other_stacks = [
                        name for name in stack_names 
                        if name != stack_name
                    ]
                    
                    # Find a destination stack that can accept this ball
                    for dest_stack in other_stacks:
                        if (len(self.stacks[dest_stack]) < self.target_stack_size and 
                            (not self.stacks[dest_stack] or 
                             self.stacks[dest_stack][0] == self.stacks[stack_name][0])):
                            self.move_ball(stack_name, dest_stack)
                            states.append(dict(self.stacks))
                            break
        
        return states