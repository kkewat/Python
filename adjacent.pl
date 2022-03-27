adjacent(1,2).
adjacent(1,3).
adjacent(1,4).
adjacent(1,5).
adjacent(2,1).
adjacent(2,3).
adjacent(2,4).
adjacent(3,1).
adjacent(3,2).
adjacent(3,4).
adjacent(4,1).
adjacent(4,2).
adjacent(4,3).
adjacent(4,5).
adjacent(5,1).
adjacent(5,4).

color(1,orange,x).
color(2,pink,x).
color(3,purple,x).
color(4,red,x).
color(5,pink,x).

color(1,orange,y).
color(2,pink,y).
color(3,purple,y).
color(4,red,y).
color(5,pink,y).

conflict(R1,R2,Coloring):-
	adjacent(R1,R2),
	color(R1,Color,Coloring),
	color(R2,Color,Coloring).

