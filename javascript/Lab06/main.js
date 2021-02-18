let app = new Vue({
    el: '#catPics',
    data: {
        catImg: '',
        cats: [],
        categories: ''
        // data goes here
    },
    methods: {
        getImage: async function(){
            let response = await axios ({
                url:'https://api.thecatapi.com/v1/images/search',
                method: 'get',
                params: {
                    category_ids: this.categories.id
                }
            })

            console.log(response.data[0].url)
            this.catImg = response.data[0].url

        }

    },
    created: async function(){
        const response = await axios({
            method: 'get',
            url: 'https://api.thecatapi.com/v1/categories'
        })
        this.cats = response.data
    }
})