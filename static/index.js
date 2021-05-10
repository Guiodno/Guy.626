document.addEventListener('DOMContentLoaded', ()=>{

    document.querySelector('.alert').style.display = 'none';

    document.querySelector('#submit').addEventListener('click' = ()=>{
        if((document.querySelector("#email").value != '') && (document.querySelector('#password')).value != ''){
            alert('connect')
            return true
        }else{
            document.querySelector('.alert').style.display = 'block';
            alert('username or password')
            return false
        }
    })

    //alert("hello,  peterson🤪")
})