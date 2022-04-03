<template>
    <section>

    <div id="fond"></div>
    <form submit="" class="connect">
        <div id="form">
            <h1 v-if="mode == 'login'">Connexion</h1>
            <h1 v-else>Inscription</h1>
            <p v-if="mode == 'login'">Tu n'as pas encore de compte ? <button id="change"><span  @click="switchToCreateAccount()">Créer un compte</span></button></p>
            <p v-else>Tu as déjà un compte ? <button id="change"><span @click="switchToLogin()">Se connecter</span></button></p>
            <div>
                <input v-model="email" type="text" placeholder="Adresse mail"/>
            </div>
            <div v-if="mode == 'create'">
                <input v-model="prenom" type="text" placeholder="Prénom"/>
                <input v-model="nom" type="text" placeholder="Nom"/>
            </div>
            <div>
                <input v-model="password" type="password" placeholder="Mot de passe"/>
            </div>
            <div v-if="mode == 'login' && status == 'error_login'">
            Adresse mail et/ou mot de passe invalide
            </div>
            <div v-if="mode == 'create' && status == 'error_create'">
            Adresse mail déjà utilisée
            </div>
            <div>
                <button @click="login()" :class="{'button--disabled' : !validatedFields}" v-if="mode == 'login'">
                    <span v-if="status == 'loading'">Connexion en cours...</span>
                    <span v-else>Connexion</span>
                </button>
                <button @click="createAccount()" :class="{'button--disabled' : !validatedFields}" v-else>
                    <span v-if="status == 'loading'">Création en cours...</span>
                    <span v-else>Créer mon compte</span>
                </button>
            </div>
        </div>
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

<script>

import { mapState } from 'vuex'

export default {
  name: 'Login',
  data: function () {
    return {
      mode: 'login',
      email: '',
      prenom: '',
      nom: '',
      password: '',
    }
  },
  mounted: function () {
    if (this.$store.state.user.userId != -1) {
      this.$router.push('/profil');
      return ;
    }
  },
  computed: {
    validatedFields: function () {
      if (this.mode == 'create') {
        if (this.email != "" && this.prenom != "" && this.nom != "" && this.password != "") {
          return true;
        } else {
          return false;
        }
      } else {
        if (this.email != "" && this.password != "") {
          return true;
        } else {
          return false;
        }
      }
    },
    ...mapState(['status'])
  },
  methods: {
    switchToCreateAccount: function () {
      this.mode = 'create';
    },
    switchToLogin: function () {
      this.mode = 'login';
    },
    login: function () {
      const self = this;
      this.$store.dispatch('login', {
        email: this.email,
        password: this.password,
      }).then(function () {
        self.$router.push('/profile');
      }, function (error) {
        console.log(error);
      })
    },
    createAccount: function () {
      const self = this;
      this.$store.dispatch('createAccount', {
        email: this.email,
        nom: this.nom,
        prenom: this.prenom,
        password: this.password,
      }).then(function () {
        self.login();
      }, function (error) {
        console.log(error);
      })
    },
  }
}
</script>

<style scoped>
    .connect{
    display: flex;
    flex-direction: column;
    justify-content:space-evenly;
    padding:30px 0;
    }

    section{
        background-image:url('../assets/images/conne.jpg'); 
        background-size: 100%;
        background-repeat: no-repeat;
        height: 800px;
        
    }

    #fond{
        height: 200px;
    }
    #form{
        margin-left: 10%;
    }

    form{
        width: 600px;
        height: 450px;
        margin:auto;
        vertical-align: middle;
        border: solid 5px #442555;
        border-radius: 30px;
        background-color: rgba(122, 110, 150, 0.8);
    }

    input,button{
        margin: 2%;
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
    #change{
        width:30%;
        font-size: medium;
    }

</style>