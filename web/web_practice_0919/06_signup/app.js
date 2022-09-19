function test() {
    var p1 = document.getElementById('password').value;
    var p2 = document.getElementById('password_confirmation').value;
    if( p1 != p2 ) {
      alert("비밀번호가 일치 하지 않습니다");
      return false;
    } else{
      alert("비밀번호가 일치합니다");
      return true;
    }
  }