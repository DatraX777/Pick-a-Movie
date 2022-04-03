<template id="app">
  <div>
    <div id="navigation1" >
      <nav>
        <ul>
            <li id="log">
                <router-link to="/"><img src="../src/assets/seresty.png"></router-link>
            </li>
            <li>
                <router-link to="/liste">Films / Séries</router-link>
            </li>
            <li>
                <router-link to="/recommandations">Recommandations</router-link>
            </li>
            <li>
                <router-link to="/connexion">Connexion</router-link>
            </li>
            <li>
                <router-link to="/contact">Contact</router-link>
            </li>
        </ul>
    </nav>
    </div>
    <router-view/>
    <div id="footer">
        <ul>
            <li>
                <a href="https://www.facebook.com/"><img src="../src/assets/images/footer1.png"></a>
            </li>
            <li>
                <a href="https://twitter.com/"><img src="../src/assets/images/footer2.png"></a>
            </li>
            <li>
                <a href="https://www.instagram.com/"><img src="../src/assets/images/footer3.png"></a>
            </li>
        </ul>
        <a href="http://localhost:8080/recommandations/">Découvrez vos recommandations!</a>
        <a href="http://localhost:8080/contact/">Contactez-nous</a>
    </div>
  </div>  
</template>

<style>

    body{
        background-color: #473f5a;
        margin : 0px;
        font-family: Arial, Helvetica, sans-serif;
        font-weight: bold;
        color: white;
    }
    a {
    color: white;
    }

</style> 
<style scoped>

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding-top: 110px;
}
section{
    margin:110px 0 0 0 !important;
}


nav>ul{
    flex-flow: row wrap-reverse;
    text-align: center;
    height: 110px;
}


ul{
    display:flex;
    flex-flow: row wrap-reverse;
    padding-left: 0px;
    margin: 0px;
    position: 0px;
}

nav>ul>li{
    list-style: none;
    margin: 0px 50px;
    vertical-align: middle;
}



nav>ul>li:not(#log){
    margin: 35px 50px
}



a,#log{
    text-decoration: none;
    font-size: 30px;
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
    position: fixed;
    top: 0px;
    width: 100%;
    background-color: #442555;
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

#footer {
    display: flex;
    justify-content: space-between;
    text-align: center;
    margin: 0 5%;
}

#footer>a {
    color: white;
    margin: 0 40px;
    font-size: 16px;
    text-transform: uppercase;

}

 #footer>p, #footer>a {
    margin-top: 1.5%;
}

#footer img {
    width: 50px;
	height: 50px;
    position: relative;
    border-radius: 10px;
   }

#footer li {
    display: inline;
    margin: 16px
   }
</style>
