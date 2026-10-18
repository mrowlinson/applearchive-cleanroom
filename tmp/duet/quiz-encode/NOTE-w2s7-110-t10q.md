# NOTE-w2s7-110-t10q (encode-writer2, own-side heartbeat)

- Shipped `4365e9e` T10DIP pair + A + 74-band (head10 + 4x16) + B + Q 15x16, N=16737..17084 (2274 pins, GREEN, 0 dropped).
- Q reuses T10BT tab + BQT[q+1] word bytes; own (b5,b11,b40,b41)[q]; b5 m>=3 q3/q11.
- Transcription audit lesson (3rd strike): programmatic table-vs-dump audit BEFORE verify loops — caught 13 mis-split bytes (dd/fd/5d/7d/bd/3d class).
- Next: map 17085+ (tabbreak).
