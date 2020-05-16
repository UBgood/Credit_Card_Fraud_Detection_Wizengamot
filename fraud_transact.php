<?php
$hostname="localhost"; //local server name default localhost

$username="root";  //mysql username default is root.

$password="";       //blank if no password is set for mysql.

$database="student1";  //database name which you created

$con=mysql_connect($hostname,$username,$password);

if(! $con)
{
die('Connection Failed'.mysql_error());
}

mysql_select_db($database,$con);
If(isset($_REQUEST['submit'])!='')
{
If($_REQUEST['name']=='')
{
Echo "please fill the empty field.";
}
Else
{
$sql="insert into student1(name) values('".$_REQUEST['name']."')";
$res=mysql_query($sql);
If($res)
{
//Echo "Fradaulent";
}

}
}

?>


<!DOCTYPE html>
<html>
    <head> <meta http-equiv="refresh" content="5">
    <style>
.myDiv {
    
    border: 2px solid black;
  outline: cornsilk solid 10px;
  margin: auto;  
  padding: 20px;
  text-align: center;
    
}
        
        .mDiv {
    
    padding-top: 240px;
  
        </style>
    </head>
<body>
<div class="mDiv"></div>

<div class="myDiv">
<form action="trans.php">
 
  <input type="text" id="name" name="name" value="Fraudulent Transaction" placeholder="Fraudulent Transaction"><br>
<script language="JavaScript">document.myform.submit();</script>
 
</form>
    
 </div>
</body>
</html>

<?php 
function function_alert($message) { 
      echo "<script>alert('$message');</script>"; 
} 
function_alert("Fraudulent Transaction notified to Bank server");
?>



