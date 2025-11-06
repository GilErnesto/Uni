# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)

    # Put your code here
    with open('aula06/drawing.txt', 'r') as fin:
        for line in fin:
            line = line.strip()
            if line == 'UP':
                t.up()
            elif line == 'DOWN':
                t.down()
            else:
                x,y = line.split()
                x, y = int(x), int(y)
                t.goto(x,y)

    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()

