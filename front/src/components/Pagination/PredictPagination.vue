<template lang="">
    <div class="pagination-container">
        <div class="pagination-content">
            <label for="listPageSize">Ligne par page </label>
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
            <jw-pagination
                :pageSize="parseInt(pageSize)" 
                :items="dataToPaginate" 
                @changePage="onChangePage" 
                :labels="customLabels" 
                :styles="customStyles"
                :key="pageSize"
            >
            </jw-pagination> 
        </div>
    </div>
</template>

<script>
    const customLabels = {
        first: '<<',
        last: '>>',
        previous: '<',
        next: '>'
    };

    const customStyles = {
        ul: {
            display: 'flex',
            alignItems: 'center',
        },
        li: {
            display: 'block',
            
        },
        a: {
            border: 'none',
            textDecoration: 'none !important',
            '&:hover': {
                textDecoration: 'none',
            },
            
        },
    };

    export default {
        name: "PredictPagination",
        props:['dataToPaginate'],
        data: () => {
            return {
                customLabels,
                customStyles,
                pageSizeList: [2, 3, 5, 10, 15, 20,  30, 50],
                pageSize: 10,
            }
        },
        methods: {
            onChangePage(dataPageOfItems){
                this.pageOfItems = dataPageOfItems;
                this.$emit("onChangePage", this.pageOfItems);
            },
        }
    }
</script>

<style>
    .pagination-content {
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .pagination-content label {
        color: #242c36;
        font-size: 12px;
        margin: 0 8px 0 0;
    }
    @media (max-width: 600px) {
        .pagination-content label {
            display: none;
        }
    }
    .pagination-content .select-field {
        position: relative;
    }
    .pagination-content #listPageSize {
        border: none;
        font-size: 12px;
        color: #242C36;
        min-width: 25px;
    }
    .pagination-content #listPageSize:focus {
        outline: none;
    }
    @media (max-width: 600px) {
        .pagination-content .pagination {
            flex-wrap: wrap;
            justify-content: center;
        }
    }
    .pagination-content .pagination .page-item .page-link {
        border: none;
        border-radius: 0 !important;
        color: #242c36 !important;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
        letter-spacing: -3px;
        padding: 0 5px !important;
        height: 18px;
        margin: 0 2px;
        min-width: 18px;
        text-align: center;
    }
    .pagination-content .pagination .page-item .page-link:hover {
        background: none;
    }
    .pagination-content .pagination .page-item.disabled .page-link {
        opacity: 0.5;
    }
    .pagination-content .pagination .page-number {
        /* min-width: 100px; */
    }
    .pagination-content .pagination .page-number .page-link {
        background-color: transparent;
        color: rgba(36, 44, 54, 0.5);
        font-size: 12px;
        font-weight: 400;
        letter-spacing: unset;
    }
    .pagination-content .pagination .page-number.active .page-link {
        color: #242c36;
        font-weight: 600;
    }

</style>