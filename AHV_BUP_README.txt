

[1] ssh certificate をcopy済みである事。
[2] remote linux host上に sshpassがinstallされていること。
[3] remote linux host上の user accountは sudoersに登録されており、
    mount/umount等の実行が許可されている事。
[4] target linux host上にdatastore をNFS mountするためのmounting pointが存在する事。
    (後で、存在しない場合には作成する様にプログラムを作成する)
