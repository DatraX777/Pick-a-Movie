<template>
  <section >
    <div id="im">
        
        <div id="fond">
            <h1>Les Cookies plus qu'une passion, des valeurs!</h1>
            <p>
            La Cabane à Cookie est spécialisée dans la commercialisation de Cookies moelleux à l'intérieur et croustillants à l'extérieur ! 
            C'est depuis fin 1989, au cœur de la capitale Pyrénéenne (PAU), 
            que la fondateur URRUTY Vincent crée et met au point des recettes uniques, développe une délicieuse expérience client, et affine un management ambitieux.
            En 2020, elle a su saisir les opportunités dans l'incertitude, la mise en place du Click & Collect et des envois sur toute la France ont été des étapes clefs 
            pour être au plus proche des clients, et être en adéquation avec l'évolution des différents canaux de distribution. 
            </p>
            <p>
            Notre priorité est aussi de favoriser les producteurs locaux, c'est pour cela que nous utilisons presque uniquement des produits Bio de nos régions 
            pour élaborer nos cookies. 
            </p>
        </div>
        
    </div>

    <div id="actu">
        <div id="title">
            <h1>Les Cookies du moment &nbsp;&nbsp; &rarr;</h1>
            <h1>Attention ils ne seront disponibles qu'un mois! <br>Venez vite en achetez!</h1>
            <p class="prix">
                Le prix à l'unité est de : 2.5€<br>
                <br>
                Les 3 pour : 7€ <br>
                <br>
                Les 5 pour : 10€ <br>
            </p>
        </div>
        <div id="item">
            <article> <!-- *ngFor="let c of cooServ.listeCookiesSpe" style="background-image:url('{{c.photo}}')" > -->
                <div id="dark">
                <ul class="info">
                   <!-- <h3>{{c.nom }}</h3>-->
                    
                    <li>
                        <details>
                            <summary>Liste des ingrédients pour 6 personnes :</summary>
                            <ul id="ingre">
                                <!--<li *ngFor="let i of c.ingredients">
                                    {{i}}
                                </li>
                                -->
                            </ul>
                        </details>
                    </li>
                </ul>
            </div>
            </article>
        </div>
    </div>
    <hr>
  </section>
</template>

<style scoped>

  #im{
    background-image:url('../assets/images/cont.jpg'); 
    background-size: 100%;
    background-repeat: no-repeat;
    height: 600px;
    align-items:center;
    text-align: center;
  }

  #fond{
      color:white;
      height: 400px;
      padding: 100px 20%;
      background-color: rgba(68, 37, 85, 0.4); 
      display: flex;   
      flex-direction: column;
  }

  p{
      margin-top: 4%;
      font-size: 20px;
  }

  #actu{
      margin: 6% 0;
      text-align: center;
      display: flex;
      grid-template-columns: repeat(12,1fr);
      color: white;
  }

  .prix{
      text-align: left;
      margin-top: 10%;
      margin-left: 20%;
  }

  ul{
      padding-inline-start: 10px;
  }

  #title{
      margin: 0% 4%;
      width: 40%;
      height: 350px;
      background-color: #442555;
      border-radius: 50px;
  }
  #item{
      width: 55%;
      display: flex;
      color: white;
      font-size: 1.2em;
  }

  details{
      display: none;
  }
  article{
      height: 400px;
      width: 10%;
      border-radius: 30px;
      border: solid 5px #442555;
      margin: 0px 30px;
      transition: width 0.5s ease;
      writing-mode: vertical-lr;
      text-orientation: sideways;
  }

  article:hover{
      width:44%;
      writing-mode: horizontal-tb;
      background-color: rgba(68, 37, 85, 0.8) ;
  }
  article:hover details{
      display: block;
      align-content: flex-end;
      text-align: left;
      margin-left: 0px;
  }

  li{
      list-style: none;
      text-decoration: none;
  }


  hr{
      margin-top: 30px;
      border-color: #442555;
  }

  img{
      width: 100px;
      border-radius: 30px;
      border: solid 5px #442555;
  }

  #log{
      width: 300px;
      object-fit: contain;
      margin: 0 5%;
      border: none;
  }


</style>
  
<script>
// @ is an alias to /src

</script>
