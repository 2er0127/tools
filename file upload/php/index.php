<?php
    header("Content-Type: text/html; charset=UTF-8");
?>

<form action="upload.php" method="POST" enctype="multipart/form-data"> <!-- input type="file" 을 사용할 때  enctype="mutipart/form-data" 를 사용한다. -->
    <input type="file" name="userfile">
    <input type="submit" value="UPLOAD">
</form>
