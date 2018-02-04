<template>
  <div id="app">
    <div class="container">
      <h1 class="title">Message Board</h1>
         <form action="/api/messages" method="POST" @submit.prevent="onSubmit" @keydown="form.errors.clear($event.target.name)">
		<div :class="['form-group',{'has-errors': form.errors.has('name')}]">
		   <input type="text" class="form-control" name="name" placeholder="Name" v-model="form.name">
		   <span class="help-block" v-if="form.errors.has('name')" v-text="form.errors.get('name')"></span>
		</div>
		<div :class="['form-group',{'has-error': form.errors.has('name')}]">
		   <textarea class="form-control" name="text" rows="5" placeholder="Say something..." v-model="form.text"></textarea>
		   <span class="help-block" v-text="form.errors.get('text')"></span>
		</div>

		<button class="btn btn-default" :disabled="form.errors.any()">Submit</button>
	</form>
	<div class="messages-header">{{ messages.length }} messages</div>
		<div class="messages">
		   <ul transition="fade">
			<template v-for="message in messages">
			   <message-item :message="message"></message-item>
			</template>
		   </ul>
		</div>
	</div>
    </div>
  </div>
</template>

<script>
import MessageItem from './components/MessageItem.vue'

class Errors{
    constructor(){
        this.errors = {}
    }
    has (field){
        return this.errors.hasOwnProperty(field)
    }
    any(){
        return Object.keys(this.errors).length > 0
    }

    get(field) {
        if (this.errors[field]) {
            return this.errors[field][0]
        }
    }

    record(errors){
        this.errors = errors
    }
    clear(field){
        delete this.errors[field]
    }
}

class Form{
    constructor(data){
        this.originalData = data

        for (let field in data){
            this[field] = data[field]
        }

        this.errors = new Errors()
    }

    data(){
    let data = {}

    for (let property in this.originalData){
        data[property] = this[property]
    }
    return data
    }
    reset(){
        for (let field in this.originalData){
            this[field] = ''
        }
        this.errors.clear()}

    submit(requestType, url){
        return new Promise((resolve, reject) => {
            http[requestType](url, this.data())
            .then(response =>{
                this.onSuccess(response.data)
                resolve(response.data)
            })
            .catch(error => {
            this.onFail(error.response.data)
            reject(error.response.data)
            })
        })
    }
    onSuccess(data){
        this.reset()
        }
    onFail(errors){
        this.errors.record(errors)
    }
    post(url){
        return this.submit('post', url)
    }

}

    export default{
    name: 'app',
    data(){
        return {
        form: new Form({name:'', text:''}),
        messages: [],
        }
    },

    methods: {
        onSubmit() {
           this.form.post('/api/messages')
           .then(data => this.messages.unshift(data))
           .catch(errors => {})
        }
    },
    mounted(){
        http.get('/api/messages')
            .then(response => this.messages = response.data)
    },

    components: { MessageItem }
}


</script>


<style>
.container{
    width: 650px;
    margin-top: 60px;
}

#app{
    margin-top: 60px;
    margin: 0 auto;
}

.title{
    text-align: center;
    margin-bottom: 20px;
    color: #e3e3e3;
}

.messages-header{
    line-height: 1;
    color: #666;
    padding: 20px 0 6px;
    border-bottom: 1px solid #eee;
    text-transform: uppercase;
    font-size: 13px;
}

.message ul{
    margin: 0;
    padding: 0;
}
</style>
