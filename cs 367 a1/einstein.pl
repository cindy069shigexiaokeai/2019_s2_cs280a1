%Einstein's five differnet houses riddle
:- use_rendering(table,
		 [header(h('Nation', 'Color', 'Pet', 'Smoke', 'Drink'))]).
next(A, B, Ls) :- 
    append(_, [A,B|_], Ls).
next(A, B, Ls) :- 
    append(_, [B,A|_], Ls).
ownerOfFish(Persons, Owner) :-
    solution(Persons),
	member(h(Owner,_,fish,_,_), Persons).
solution(Persons) :-
    length(Persons, 5),
    member(h(brit,red,_,_,_), Persons),
	member(h(swede,_,dogs,_,_), Persons),
    member(h(dane,_,_,_,tea), Persons),
    next(h(_,green,_,_,_),h(_,white,_,_,_), Persons),
    member(h(_,green,_,_,coffee), Persons),
    member(h(_,_,birds,pallmall,_), Persons),
    member(h(_,yellow,_,dunhill,_), Persons),
    Persons = [_,_,h(_,_,_,_,milk),_,_],
    Persons = [h(norwegian,_,_,_,_),_,_,_,_],
    next(h(_,_,_,blends,_),h(_,_,cats,_,_), Persons),
    next(h(_,_,horses,_,_),h(_,_,_,dunhill,_), Persons),
    member(h(_,_,_,bluemaster,beer), Persons),
    member(h(german,_,_,prince,_), Persons),
    next(h(norwegian,_,_,_,_), h(_,blue,_,_,_), Persons),
    next(h(_,_,_,blends,_), h(_,_,_,_,water), Persons),
    member(h(_,_,fish,_,_), Persons).

    


