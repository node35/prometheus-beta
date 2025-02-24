from typing import List, Literal

Color = Literal['Red', 'Blue', 'Green']

class ColorStackSorter:
    def __init__(self, red_stack: List[Color], blue_stack: List[Color], green_stack: List[Color]):
        """
        Initialize the color stack sorter with three stacks of colored balls.
        
        Args:
            red_stack (List[Color]): Stack of red balls
            blue_stack (List[Color]): Stack of blue balls
            green_stack (List[Color]): Stack of green balls
        """
        if not (len(red_stack) == len(blue_stack) == len(green_stack)):
            raise ValueError("All stacks must have an equal number of balls")
        
        self.stacks = {
            'Red': red_stack,
            'Blue': blue_stack,
            'Green': green_stack
        }
        self.moves = []
    
    def move_ball(self, source: Color, destination: Color) -> None:
        """
        Move a single ball from source stack to destination stack.
        
        Args:
            source (Color): Color of the source stack
            destination (Color): Color of the destination stack
        
        Raises:
            ValueError: If source stack is empty or source and destination are the same
        """
        if source == destination:
            raise ValueError("Source and destination stacks must be different")
        
        if not self.stacks[source]:
            raise ValueError(f"No balls left in {source} stack")
        
        ball = self.stacks[source].pop()
        self.stacks[destination].append(ball)
        self.moves.append((source, destination))
    
    def is_sorted(self) -> bool:
        """
        Check if all stacks have only their respective color.
        
        Returns:
            bool: True if sorted, False otherwise
        """
        for color, stack in self.stacks.items():
            if any(ball != color for ball in stack):
                return False
        return True
    
    def sort(self) -> List[tuple]:
        """
        Sort the stacks so that each stack contains only its respective color.
        
        Returns:
            List[tuple]: List of moves made during sorting
        """
        stack_colors = list(self.stacks.keys())
        
        while not self.is_sorted():
            # Find the color that is not in its correct stack
            for color in stack_colors:
                if any(ball != color for ball in self.stacks[color]):
                    # Move incorrect balls
                    for other_color in stack_colors:
                        if other_color != color:
                            # Move incorrect balls to other stacks
                            while any(ball != color for ball in self.stacks[other_color]):
                                self.move_ball(other_color, color)
                                break
        
        return self.moves