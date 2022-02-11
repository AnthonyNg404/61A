(cdr '(1 2 4 6 2 4))

(define (news s last)
    (if (> last (car s))
    s
    (news (cdr-stream s) (car s))))

(news '(1 2 4 6 2 4) 1)

    (define (news s last)
        (if (null? s)
            nil
            (if (> last (car s))
            s
            (news (cdr-stream s) (car s)))))
    (if (null? s)
        nil
        (cons-stream (nondecrease s (car s)) (nondecreastream (news s (car s)))))