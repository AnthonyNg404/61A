(define new '((2 3) (2 4) (3 5))) 
(car new)
(define a (cons 1 (car '((2 3) (2 4) (3 5)))))
a
(cdr a)

(define (cons-all first rests)
  (if (null? (cdr rests))
          (list (cons first (car rests)))
          (append (list (cons first (car rests)))
                   (cons-all first (cdr rests)))))
(cons-all 1 '((2 3) (2 4) (3 5)))
(append '(1) '(2 3))

