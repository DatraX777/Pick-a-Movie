<template>
  <section>
    <div id="be">
    <h2>Contactez-nous!</h2>
      <p>Avez-vous des questions? N'hésitez pas à nous contacter directement. Notre équipe reviendra vers vous dans les heures qui suivent pour vous aider.</p>
    </div>
    <div id="fo">
        <form id="contact-form" name="contact-form" method="POST">
            <input type="text" id="name" name="name" placeholder="Indiquez votre nom/prénom">
            <input type="text" id="email" name="email" placeholder="Indiquez votre email">
            <input type="text" id="subject" name="subject" placeholder="Indiquez votre sujet">
            <textarea type="text" id="message" name="message" rows="10" cols="60" placeholder="Rédigez votre message" ></textarea>
            <input type="submit" value="Envoyer" >
        </form>
    </div>
    <div id="end">
        <ul>
            <li>
                <p>10 Boulevard Alsace Lorraine, PAU, France</p>
            </li>
            <li>
                <p>02 08 03 14 15</p>
            </li>
            <li>
                <p>CabaneACookie@gmail.com</p>
            </li>
        </ul>
    </div>
  </section>
</template>

<style scoped>

    section{
        background-color: #473f5a;
        color: white;
        font-family: Arial, Helvetica, sans-serif;
        font-weight: bold;  
    }

    #fo{
        background-image:url('../assets/images/cont.jpg'); 
        background-size: 100%;
        background-repeat: no-repeat;
        height: 700px;
        display: flex;
        flex-direction: column;
        align-items:center;
        font-size: large;
    }

    #end,#be{
        padding-top: 1%;
        margin: 0 25% 3% 25%;
        text-align: center;
        font-size: x-large;
    }

    li{
        text-decoration: none;
        list-style: none;
    }

    form{
        width: 700px;
        height: 500px;
        margin:auto;
        display: flex;
        flex-direction: column;
        align-items:center;
        justify-content: space-evenly;
        border: solid 5px #442555;
        border-radius: 30px;
        background-color: rgba(71,63,90,.8);
    }

    input,button{
        width: 50%;
        height: 40px;
        border:2px solid #442555;
        color: white;
        font-size: large;
        background-color: #442555;
    }

    input[type=submit],input[type=reset]{
        border-radius: 10px;
        width: 25%;
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
