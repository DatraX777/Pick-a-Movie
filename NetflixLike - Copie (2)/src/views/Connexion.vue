<template>
    <section>

    <div id="fond"></div>
    <form submit="" class="connect">
        <!-- ngmodel est un élément permettant la mise a jour dans les deux sens des données (component - html )-->
        <input type="text" name="id" placeholder="Saisissez un identifiant" >
        <input name="mdp" placeholder="Saisissez un mot de passe" type="password">
        <input type="submit" value="envoyer" >
        <input type="reset" value="annuler">
    </form>
    <!--
    <div id="fond">
        <form class="connect">
            <button click="deconnect()">Se déconnecter</button>
        </form>
    </div>
    -->
    </section>
</template>

<style scoped>
    .connect{
    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content:space-evenly;
    padding:30px 0;
    }

    section{
        background-image:url('../assets/images/conne.jpg'); 
        background-size: 100%;
        background-repeat: no-repeat;
        height: 800px;
        align-items:center;
    }

    #fond{
        height: 200px;
    }

    form{
        width: 500px;
        height: 300px;
        margin:auto;
        vertical-align: middle;
        border: solid 5px #442555;
        border-radius: 30px;
        background-color: rgba(122, 110, 150, 0.8);
    }

    input,button{
        width: 50%;
        height: 40px;
        border: 2px solid #442555;
        color: white;
        font-size: large;
        background-color: #442555;
    }

    input[type=submit],input[type=reset]{
        border-radius: 10px;
        width: 25%;
        cursor: pointer;
    }
    button{
        border-radius: 10px;
        cursor: pointer;
    }
    input[type=submit]:hover,input[type=reset]:hover,button:hover{
        border: 2px solid white;
    }

    ::placeholder {
        color: white;
    }

    input[type=number]:focus,input[type=text]:focus,input[type=password]:focus{
        border: 2px solid white;
        border-radius: 5px;
        outline: none;
    } 

</style>