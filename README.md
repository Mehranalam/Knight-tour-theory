# Knight-tour-theory
A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square exactly once. If the knight ends on a square that is one knight's move from the beginning square (so that it could tour the board again immediately, following the same path), the tour is closed (or re-entrant); otherwise, it is open

## من از روش Divide-and-conquer algorithms

با تقسیم تخته به قطعات کوچکتر، ساختن تورهای روی هر قطعه، و وصله کردن قطعات به هم، می توان تورهایی را بر روی اکثر تخته های مستطیلی در زمان خطی ایجاد کرد - یعنی در زمانی متناسب با تعداد مربع های روی تخته.

By dividing the board into smaller pieces, constructing tours on each piece, and patching the pieces together, one can construct tours on most rectangular boards in linear time – that is, in a time proportional to the number of squares on the board.
