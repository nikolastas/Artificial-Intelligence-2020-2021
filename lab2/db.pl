find_sim_1(X, Y):- 
genre(X, G1), 
genre(Y, G1), 
X \= Y.

find_sim_2(X,Y):-
genre(X,G1),
genre(X,G2),
G2 \= G1,
genre(Y,G1),
genre(Y,G2),
X \= Y.

find_sim_3(X,Y):-
genre(X,G1),
genre(X,G2),
G2 \= G1,
genre(X,G3),
G3 \= G1,
G3 \= G2,
genre(Y,G1),
genre(Y,G2),
genre(Y,G3),
X \= Y.

find_sim_4(X,Y):-
genre(X,G1),
genre(X,G2),
G2 \= G1,
genre(X,G3),
G3 \= G1,
G3 \= G2,
genre(X,G4),
G4 \= G1,
G4 \= G2,
G4 \= G3,
genre(Y,G1),
genre(Y,G2),
genre(Y,G3),
genre(Y,G4),
X \= Y.

find_sim_5(X,Y):-
genre(X,G1),
genre(X,G2),
G2 \= G1,
genre(X,G3),
G3 \= G1,
G3 \= G2,
genre(X,G4),
G4 \= G1,
G4 \= G2,
G4 \= G3,
genre(X,G5),
G5 \= G1,
G5 \= G2,
G5 \= G3,
G5 \= G4,
genre(Y,G1),
genre(Y,G2),
genre(Y,G3),
genre(Y,G4),
genre(Y,G5),
X \= Y.

common_director(X,Y):-
director_name(X,N1),
director_name(Y,N1),
X \= Y.

sim_plot_5(X,Y):-
plot_keywords(X,G1),
plot_keywords(X,G2),
G2 \= G1,
plot_keywords(X,G3),
G3 \= G1,
G3 \= G2,
plot_keywords(X,G4),
G4 \= G1,
G4 \= G2,
G4 \= G3,
plot_keywords(X,G5),
G5 \= G1,
G5 \= G2,
G5 \= G3,
G5 \= G4,
plot_keywords(Y,G1),
plot_keywords(Y,G2),
plot_keywords(Y,G3),
plot_keywords(Y,G4),
plot_keywords(Y,G5),
X \= Y.

sim_plot_4(X,Y):-
plot_keywords(X,G1),
plot_keywords(X,G2),
G2 \= G1,
plot_keywords(X,G3),
G3 \= G1,
G3 \= G2,
plot_keywords(X,G4),
G4 \= G1,
G4 \= G2,
G4 \= G3,
plot_keywords(Y,G1),
plot_keywords(Y,G2),
plot_keywords(Y,G3),
plot_keywords(Y,G4),
X \= Y.

sim_plot_3(X,Y):-
plot_keywords(X,G1),
plot_keywords(X,G2),
G2 \= G1,
plot_keywords(X,G3),
G3 \= G1,
G3 \= G2,
plot_keywords(Y,G1),
plot_keywords(Y,G2),
plot_keywords(Y,G3),
X \= Y.


sim_plot_1(X,Y):-
plot_keywords(X,G1),
plot_keywords(Y,G1),
X \= Y.


sim_plot_2(X,Y):-
plot_keywords(X,G1),
plot_keywords(X,G2),
G2 \= G1,
plot_keywords(Y,G1),
plot_keywords(Y,G2),
X \= Y.

sim_actor_base(X, Y):- 
actor_1_name(X, G1), 
actor_1_name(Y, G1), 
X \= Y.


sim_actor_1(X,Y):-
actor_name(X,G1),
actor_name(Y,G1),
X \= Y.


sim_actors_2(X,Y):-
actor_name(X,G1),
actor_name(X,G2),
G2 \= G1,
actor_name(Y,G1),
actor_name(Y,G2),
X \= Y.


sim_actors_3(X,Y):-
actor_name(X,G1),
actor_name(X,G2),
G2 \= G1,
actor_name(X,G3),
G3 \= G1,
G3 \= G2,
actor_name(Y,G1),
actor_name(Y,G2),
actor_name(Y,G3),
X \= Y.

sim_lang(X,Y):-
language(X,L),
language(Y,L),
X \= Y.

sim_color(X,Y):-
plot_keywords(X,"black and white"),
plot_keywords(Y,"black and white"),
X \= Y.
sim_color(X,Y):-
not(plot_keywords(X,"black and white")),
(plot_keywords(Y,G1)),
 G1 \= "black and white",
X \= Y.

sim_studio(X,Y):-
production_companies(X,C1,_),
production_companies(Y,C1,_),
X \= Y.

sim_count(X,Y):-
production_countries(X,_,_,C1),
production_countries(Y,_,_,C1),
X \= Y.

same_dec(X,Y):-
    title_year(X,L0),
    atom_number(L0,L),
    L1 is div(L,10),
    L2 is L1*10,
    title_year(Y,L6),
    atom_number(L6,L3),
    L3 >=L2,
    L4 is (L2 + 9),
    L3 =< L4,
    X \= Y.

