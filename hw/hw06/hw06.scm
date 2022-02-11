;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)))

(define (caddr s)
  (car (cdr (cdr s))))

(define (sign x)
  (cond ((= x 0) 0) ((< x 0) -1) (else 1)))

(define (square x) (* x x))

(define (pow b n)
  (cond ((even? n) (square (pow b (/ n 2)))) ((= n 1) b) (else (* b (pow b (- n 1))))))

(define (unique s)
  (define b nil)
  (define (search b l)
      (cond 
            ((null? b)
                    0) 
            ((eq? (car b) l)
                    1) 
            (else 
                  (search (cdr b) l))))
  (define (add s b)
      (cond 
            ((null? s) 
                b)
            ((eq? (search b (car s)) 1) 
                (add (cdr s) b)) 
            (else
                (define b (append b (cons (car s) nil))) 
                (add (cdr s) b))))
  (add s b)
  )

(cons 1 '(list 2 3))