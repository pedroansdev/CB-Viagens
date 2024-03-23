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

// Declaration of some variabels: the value of ModalOpen(for its operation) and the services that will be got with the axios.get
var services = ref([])
var confService = ref(null)
var econService = ref(null)
var isModalOpen = ref(false)

async function getServices() {
    // Gets html form elements for comparisons
    var dateInput = document.getElementById("date").value
    var selectInput = document.getElementById("cities")
    var selectedValue = selectInput.options[selectInput.selectedIndex].value;

    // Checks if the form is empty 
    if (selectedValue == '' || dateInput == '') {
        isModalOpen.value = true
    } else {
        // Axios obtains the endpoint according to the value that was selected in the form
        axios.get(`/${selectedValue}`).then((response) => {
            services.value = response.data

            // Arranges the list in ascending order according to the duratiion of the travel 
            confService.value = services.value.slice().sort((a, b) => {
                const durA = parseFloat(a.duration.replace('h', ''))
                const durB = parseFloat(b.duration.replace('h', ''))
                return durA - durB
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

function closeModal() {
    isModalOpen.value = false
}

function clear() {
    // Reload the page and clear all its data
    location.reload()
}
</script>

<template>
    <header class="bg-white shadow-lg min-w-full h-16 "></header>

    <!-- Sidebar -->
    <div
        class="fixed top-0 bottom-0 p-2 overflow-y-auto text-center bg-cb-gray flex flex-col p-4 pt-6 space-y-16 w-1/6">
        <img src="../assets/img/logo.png" alt="CBViagens logo">
        <div class="flex flex-row items-center space-x-1">
            <img src="../assets/img/calculator-edited.png" alt="Calculator Icon" width="16px">
            <p class="text-cb-white font-semibold">Calculadora de Viagem</p>
        </div>
    </div>

    <!-- Form and result section -->
    <div class="ml-56 mt-16">
        <div class="grid grid-cols-5 mx-auto w-11/12 gap-4 shadow-xl rounded-b-md">

            <!-- The topbar of the form where the tool title is -->
            <div class="col-span-5 bg-cb-gray pl-6 py-2 rounded-t-md h-16 flex items-center space-x-2">
                <img src="../assets/img/truck-edited.png" alt="Truck Icon" width="40px">
                <p class="text-cb-white text-xl font-semibold">Calculadora de Viagem</p>
            </div>

            <!-- Form section -->
            <div class="col-span-2 ml-2 pt-4 pb-6">
                <div class="bg-cb-light-gray p-4 rounded-lg flex flex-col items-center space-y-4">
                    <!-- Title of the form -->
                    <div class="flex flex-row items-center space-x-2">
                        <img src="../assets/img/earnings-edited-black.png" alt="Earnings Icon" width="30px">
                        <p class="text-xl font-semibold text-cb-gray">Calcule o Valor da Viagem</p>
                    </div>

                    <!-- Form -->
                    <form action="" v-on:submit.prevent="getServices()" class="flex flex-col space-y-2">
                        <label for="cities" class="text-sm font-bold text-cb-gray-600">Destino</label>
                        <select name="cities" id="cities" class="w-80 p-2 rounded-md text-cb-gray-600">
                            <!-- Iterates over each option to implement the select -->
                            <option v-for="option in options" :value="option.value">{{ option.city }}
                            </option>
                        </select>
                        <label for="date" class="text-sm font-semibold text-cb-gray-600">Data</label>
                        <input type="date" name="date" id="date" class="w-80 p-2 rounded-md text-cb-gray-600">
                        <div class="text-center">
                            <button type="submit"
                                class="bg-cb-blue rounded-md text-center px-8 py-1 w-1/2">Buscar</button>
                        </div>
                    </form>

                </div>
            </div>
            <!-- The result section -->
            <div class="col-span-3">
                <!-- If the person doesn't make any request, this div is loaded -->
                <div v-if="confService === null && econService === null"
                    class="min-h-full flex items-center justify-center">
                    <div>
                        <!-- Informative text -->
                        <p class="text-xl font-semibold text-cb-gray.">Nenhum dado selecionado.</p>
                    </div>
                </div>
                <!-- If the person makes any request, this div is loaded instead of the other -->
                <div v-else>
                    <div class="flex flex-col justify-left space-y-4 mb-4">
                        <!-- Title of the section -->
                        <p class="text-xl font-semibold text-cb-gray">Estas são as melhores alternativas de <br> viagem
                            para a data selecionada</p>
                        <div class="flex flex-row space-x-2 mr-4">
                            <!-- General informations card of the most expensive service -->
                            <div class="bg-cb-light-gray w-1/2 flex flex-row rounded-r-md basis-3/4">
                                <div class="flex items-center p-4 bg-cb-blue rounded-l-md">
                                    <img src="../assets/img/earnings-edited.png" alt="Earnings Icon" width="40px">
                                </div>
                                <div class="p-4 rounded-r-md">
                                    <p class="text-lg font-semibold">{{ confService[0].name }}</p>
                                    <p>Leito: {{ confService[0].bed }} (Completo)</p>
                                    <p>Tempo estimado: {{ confService[0].duration }}</p>
                                </div>
                            </div>
                            <!-- Price card -->
                            <div class="bg-cb-light-gray rounded p-4 flex flex-col basis-1/4">
                                <p class="text-lg font-semibold">Preço</p>
                                <p>{{ confService[0].price_confort }}</p>
                            </div>
                        </div>
                        <div class="flex flex-row space-x-2 mr-4">
                            <!-- General informations card of the most economical service -->
                            <div class="bg-cb-light-gray w-1/2 flex flex-row rounded-r-md basis-3/4">
                                <div class="flex items-center p-4 bg-cb-blue rounded-l-md">
                                    <img src="../assets/img/clock_check-edited.png" alt="Clock Icon" width="40px">
                                </div>
                                <div class="p-4 rounded-r-md">
                                    <p class="text-lg font-semibold">{{ econService[0].name }}</p>
                                    <p>Poltrona: {{ econService[0].seat }} (Convencional)</p>
                                    <p>Tempo estimado: {{ econService[0].duration }}</p>
                                </div>
                            </div>
                            <!-- Price carg -->
                            <div class="bg-cb-light-gray rounded p-4 flex flex-col basis-1/4">
                                <p class="text-lg font-semibold">Preço</p>
                                <p>{{ econService[0].price_econ }}</p>
                            </div>
                        </div>
                        <!-- Clear Button -->
                        <div class="flex justify-end mr-4">
                            <div class="text-center">
                                <button class="bg-cb-yellow rounded-md text-center px-8 py-1"
                                    v-on:click.prevent="clear">Limpar</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal structure -->
    <div v-if="isModalOpen"
        class="fixed top-0 left-0 bottom-0 right-0 bg-cb-gray-transparent flex justify-center items-center" id="modal">
        <div class="bg-cb-white flex flex-col justify-center items-center rounded-xl w-5/12 h-2/5 space-y-4">
            <img src="../assets/img/attention-edited.png" alt="Attention Icon" width="50px">
            <p class="text-xl font-semibold text-cb-gray text-center">Insira os valores para realizar <br> a cotação.
            </p>
            <button class="bg-cb-blue rounded-md text-center px-8 py-1 font-semibold" v-on:click="closeModal"
                id="closeButton">Fechar</button>
        </div>
    </div>
</template>
