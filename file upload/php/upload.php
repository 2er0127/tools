<?php
    header("Content-Type: text/html; charset=UTF-8");

    if(empty($_FILES["userfile"]["name"])) {
        # 업로드 된 파일이 없을 경우
        echo "<script>alert('no file');history.back(-1);</script>";
        exit();
    }

    $path = "./upload/";
    $filename = $_FILES["userfile"]["name"];

    # 서버에 업로드 된 파일을 저장할 때 사용
    if(!move_uploaded_file($_FILES["userfile"]["tmp_name"], $path.$filename)) { # php에서 .은 연결 연산자
        # 업로드 실패했을 경우
        echo "<script>alert('upload fail');history.back(-1);</script>";
        exit();
    }
?>

<li>upload success: <?=$path.$filename?></li>
