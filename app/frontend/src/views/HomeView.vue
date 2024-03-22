<script setup>
import { ref, reactive } from 'vue'
import axios from 'axios'

// List of the cities for form options on select tag
const options = reactive([
    {
        city: 'Selecione o destino',
        value: ''
    },
    {
        city: 'São Paulo',
        value: 'sp'
    },
    {
        city: 'Rio de Janeiro',
        value: 'rj'
    },
    {
        city: 'Belo Horizonte',
        value: 'bh'
    },
    {
        city: 'Manaus',
        value: 'manaus'
    },
    {
        city: 'Natal',
        value: 'natal'
    },
    {
        city: 'Campinas',
        value: 'campinas'
    },
    {
        city: 'Recife',
        value: 'recife'
    },
    {
        city: 'Salvador',
        value: 'salvador'
    },
    {
        city: 'Fortaleza',
        value: 'fortaleza'
    }
])

const services = ref([])
const confService = ref(null)
const econService = ref(null)

async function getServices() {
    // Gets html form elements for comparisons
    var dateInput = document.getElementById("date").value
    var selectInput = document.getElementById("cities")
    var selectedValue = selectInput.options[selectInput.selectedIndex].value;

    // Checks if the form is empty 
    if (selectedValue == '' || dateInput == '') {
        console.log('Insira os valores para realizar a cotação')
    } else {
        // Axios obtains the endpoint according to the value that was selected in the form
        axios.get(`/${selectedValue}`).then((response) => {
            services.value = response.data

            // Arranges the list in descending order according to the price of the comfort plan 
            confService.value = services.value.slice().sort((a, b) => {
                const priceA = parseFloat(a.price_confort.replace(/[^\d.-]/g, ''))
                const priceB = parseFloat(b.price_confort.replace(/[^\d.-]/g, ''))
                return priceB - priceA
            })

            // Arranges the list in ascending order according to the price of the economic plan 
            econService.value = services.value.slice().sort((a, b) => {
                const priceA = parseFloat(a.price_econ.replace(/[^\d.-]/g, ''))
                const priceB = parseFloat(b.price_econ.replace(/[^\d.-]/g, ''))
                return priceA - priceB
            })
        })
    }
}
</script>

<template>
    <div>
        <h1>Calculadora de Viagem</h1>
        <div>
            <h2>Calcule o valor da viagem</h2>
            <form action="" v-on:submit.prevent="getServices()">
                <label for="cities">Destino</label><br>
                <select name="cities" id="cities">
                    <option v-for="option in options" :value="option.value">{{ option.city }}
                    </option>
                </select><br>
                <label for="date">Data</label><br>
                <input type="date" name="date" id="date"><br>
                <button type="submit">Buscar</button>
            </form>
        </div>
        <div>
            <div v-if="confService === null && econService === null">
                <p>Nenhum dado selecionado.</p>
            </div>
            <div v-else>
                <div>
                    <p>{{ confService[0].name }}</p>
                    <p>Leito: {{ confService[0].bed }} (Completo)</p>
                    <p>Tempo estimado: {{ confService[0].duration }}</p>
                    <p>Preço: {{ confService[0].price_confort }}</p>
                </div>
                <div>
                    <p>{{ econService[0].name }}</p>
                    <p>Poltrona: {{ econService[0].seat }} (Convencional)</p>
                    <p>Tempo estimado: {{ econService[0].duration }}</p>
                    <p>Preço: {{ econService[0].price_econ }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
