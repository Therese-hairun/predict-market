<template>
    <div class="pagination-container">
        <div class="pagination-content">
            <label for="listPageSize">{{$t("rowPerPage")}}</label>
            <div class="select-field">
                <select v-model="pageSize" id="listPageSize">
                    <option 
                        v-for="sizeValue in pageSizeList" 
                        :value="parseInt(sizeValue)" 
                        :key="sizeValue">
                        {{sizeValue}}
                    </option>
                </select>
            </div>
            <div class="pagination">
                <div class="page-item page-number mx-2">
                    <p class="m-0 page-link">{{val1}}-{{dataSize > val2 ? val2 : dataSize}} {{$t('of')}} {{dataSize}}</p>
                </div>
                <div>
                    <button class="button-pagination" v-on:click="handleDecrement" :disabled="isMin">{{previousSymbol}}</button>
                    <button class="button-pagination" v-on:click="handleIncrement" :disabled="next === null ? true : isMax">{{nextSymbol}}</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "TablePagination",
    props: ['dataSize', 'next'],
    data: () => {
        return {
            pageSizeList: [5, 10, 15, 20],
            previousSymbol: '<',
            nextSymbol: '>',
            page: 1,
            pageSize: 5,
            val1: 1,
            val2: 5,
            isMax: false,
            isMin: true,
            maxPage: 0, 
        }
    },

    watch:{
        page(val){
            this.$emit("pageVal", val);
            this.isMin = val <= 1 ? true : false;
            this.isMax = val >= this.maxPage ? true : false;
        },
        pageSize(val){
            this.$emit("pageSize", val);
            this.page = 1;
            this.val1 = 1;
            this.val2 = this.dataSize < this.pageSize ? this.dataSize: this.pageSize;
            this.isMax = this.dataSize < this.pageSize ? true : false;
        }
    },
    methods:{
        handleIncrement(){
            this.maxPage = Math.ceil(this.dataSize / this.pageSize)
            this.isMin = false;
            this.page < this.maxPage && this.page++;
            this.val1 = this.val2 + 1;
            this.val2 = this.val2 + this.pageSize < this.dataSize ? this.val2 + this.pageSize : this.dataSize;
        },
        handleDecrement(){
            this.isMax = false;
            this.page > 1 && this.page--;
            this.val2 = this.val1 - 1;
            this.val1 -= this.pageSize;
        }
    }
}
</script>
<style scoped>
   
    .pagination-content .pagination .page-number .page-link {
        font-weight: 600;
        line-height: 20px;
    }
    .pagination-content .button-pagination {
        font-family: "Poppins-Medium", sans-serif;
        line-height: 20px;
        border: none;
        border-radius: 0;
        color: #242c36;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
        letter-spacing: -3px;
        padding: 0 5px;
        height: 18px;
        margin: 0 2px;
        min-width: 18px;
        text-align: center;
        opacity: 0.5;
        background-color: transparent;
    }
    .pagination-content .button-pagination:hover {
        color: #242c36 !important;
        opacity: 1;
    }
    .pagination-content .button-pagination:disabled:hover {
        color: #242c36 !important;
        opacity: 0.5;
    }

</style>