<template>
<html>
<head>

</head>
<body>
  <div id="navigation1" >
    <nav>
        <ul>
            <li id="log">
                <img routerLink="/"  src="../assets/seresty.png">
            </li>
            <li>
                <a routerLink="/liste">Films / Séries</a>
            </li>
            <li>
                <a routerLink="/recommendations">Recommandations</a>
            </li>
            <li>
                <a routerLink="/connexion">Connexion</a>
            </li>
            <li>
                <a routerLink="/contact">Contact</a>
            </li>
        </ul>
    </nav>
</div>
</body>
</html>
</template>


<script>

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body{
    margin:0px !important;
}


:host,ul{
    flex-flow: row wrap-reverse;
    text-align: center;
    height: 110px;
}


ul{
    display:flex;
    flex-flow: row wrap-reverse;
    justify-content: space-around;
    padding-left: 0px;
    margin: 0px;
    position: 0px;
}

li{
    list-style: none;
    margin: 0px 50px;
    vertical-align: middle;
}



li:not(#log){
    margin: 35px 50px
}



a{
    padding: 8px 12px;
    color: white;
    text-decoration: none;
    font-size: 30px;
    font-weight: bold;
    font-family: Arial, Helvetica, sans-serif;
    text-transform: uppercase;
}


img{
    display:block;
    margin:auto auto;
    width:200px;
}

#log {
    width: 200px;
    cursor:pointer;
}


#navigation1,#navigation2{
    background-color: #473f5a;
    position: fixed;
    top: 0px;
    width: 100%;
}

#navigation1>nav>ul>li>a {
    position: relative;
}

#navigation1>nav>ul>li>a::after {
    content: '';
    transform-origin: 0 0; 
    transform: scaleX(0);
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: .1em; 
    background: white;
    z-index: 2;
    opacity: 0.8;
    transition: transform .3s;
}
#navigation1>nav>ul>li>a:hover::after {
    transform: scaleX(1);
}
</style>