(define (partial-sums stream)
    (define (helper index stream)
        (if (null? stream)
            nil
            (cons-stream (+ (car stream) index) (helper (+ index (car stream)) (cdr-stream stream)))))
    (helper 0 stream)
)