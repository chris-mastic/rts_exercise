class TwoMethods:

    def above_below(self, comparison, int_list):
        """
            accepts two arguments
                An unsorted collection of integers (the list)
                an integer (the comparison value)
            returns a hash/object/map/etc. with the keys "above"
            and "below" with the corresponding count of integers
            from the list that are above or below the comparison value
            Example:
                Example usage:
                    input: [1, 5, 2, 1, 10], 6
                    output: { "above": 1, "below": 4 }
        """
        abovebelow = {"above": 0, "below": 0}
        comparison_value = comparison

        for integer in int_list:
            if (integer < comparison_value):
                abovebelow["below"]+= 1
            if (integer > comparison_value):
                abovebelow["above"]+= 1

        print(f'{abovebelow}\n')
    
    def string_rotation(self, rotation, string):
        """
        accepts two arguments
            a string (the original string)
            a positive integer (the rotation amount)
        returns a new string, rotating the characters in 
        the original string to the right by the rotation amount
        and have the overflow appear at the beginning
        Example usage:
            input: "MyString", 2
            output: "ngMyStri"
        """
        string = string
        rotation = rotation

        if (rotation >= len(string)):
            print(f'ERRROR: Can only rotate a string whose length is greater than its rotation\n')
            return

        rotated = string[:-rotation]
        overflow = string[-rotation:]

        print(f'Here is the rotated string: {overflow}{rotated}\n')

    def get_integer_list(self):
        comparison = int(input("Type the comparison value and press Enter: "))
        int_list = []
        while True:
            character = input("Type in an integer and press Enter to add to list. Press Enter when done: ")
            if character.isdigit():
                integer = int(character)
                int_list.append(integer)
            else:
                print(int_list)
                self.above_below(comparison,int_list)
                break
            
       
        
        
    def get_string(self):
        string = input("Enter a string: \n") 

        rotation = int(input("Enter a positive integer to rotate string by: "))
        while rotation < 0:   
            rotation = int(input("Enter a positive integer to rotate string by: "))

        self.string_rotation(rotation, string)
    
    def main(self):
    
        while True:
            selection = int(input("Enter 1 for abovebelow\n"
            "Enter 2 to rotate a string\n" 
            "Enter any other number to quit\n"))
            if selection < 1 or selection > 2:
                break
            if selection == 1:
                self.get_integer_list()
            if selection == 2:
                self.get_string()
                #call string_rotation

if __name__ == '__main__':
    o = TwoMethods()
    o.main()
       
