find_sim_1(X, Y):- 
actor_sim(X, G1), 
actor_sim(Y, G1), 
X \= Y.

find_sim_3(X,Y):-
actor_sim(X,G1),
actor_sim(X,G2),
G2 \= G1,
actor_sim(X,G3),
G3 \= G1,
G3 \= G2,
actor_sim(Y,G1),
actor_sim(Y,G2),
actor_sim(Y,G3),
X \= Y.

find_sim_5(X,Y):-
actor_sim(X,G1),
actor_sim(X,G2),
G2 \= G1,
actor_sim(X,G3),
G3 \= G1,
G3 \= G2,
actor_sim(X,G4),
G4 \= G1,
G4 \= G2,
G4 \= G3,
actor_sim(X,G5),
G5 \= G1,
G5 \= G2,
G5 \= G3,
G5 \= G4,
actor_sim(Y,G1),
actor_sim(Y,G2),
actor_sim(Y,G3),
actor_sim(Y,G4),
actor_sim(Y,G5),
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

sim_color(X,Y):.

sim_studio(X,Y):-
production_companies(X,C1,_),
production_companies(Y,C1,_),
X \= Y.

sim_studio(X,Y):-
production_countries(X,_,_,C1),
production_countries(Y,_,_,C1),
X \= Y.

same_dec(X,Y):-
title_year(X,G1),
title_year(Y,G2),
G11 is G1+10,
G2 <= G11,
G2 > G1,
X \= Y.

same_dec(X,Y):-
title_year(X,G1),
title_year(Y,G2),
G11 is G1-10,
G2 > G11,
G2 <= G1,
X \= Y.