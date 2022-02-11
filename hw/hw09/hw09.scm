
; Tail recursion

(define (replicate x n)
    (define (replicate_tail x n s)
      	(if (= n 0)
    		s
    		(replicate_tail x (- n 1) (append (list x) s))))
    (replicate_tail x n nil)
  )

(define (accumulate combiner start n term)
    (if (= n 0)
    	start
    	(combiner (term n) (accumulate combiner start (- n 1) term)))
)

(define (accumulate-tail combiner start n term)
  (cond ((eq? combiner +)  (define current 0))
        ((eq? combiner *)  (define current 1)))
  (define (combine n current)
    (if (= 0 n)
        (combiner current start)
        (combine (- n 1) (combiner current (term n)))))
  (combine n current)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))


(define multiples-of-three
    (cons-stream 3 (map-stream (lambda (x) (+ 3 x)) multiples-of-three))
)


(define (nondecreastream s)
    (define (nondecrease s last)
        (if (null? s)
            nil
            (if (> last (car s))
            nil
            (cons (car s) (nondecrease (cdr-stream s) (car s))))))
    (define (news s last)
        (if (null? s)
            nil
            (if (> last (car s))
            s
            (news (cdr-stream s) (car s)))))
    (if (null? s)
        nil
        (cons-stream (nondecrease s (car s)) (nondecreastream (news s (car s)))))
)



(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))
                        

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))
            