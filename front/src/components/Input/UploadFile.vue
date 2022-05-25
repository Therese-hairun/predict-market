<template>
  <div class="upload-file w-100">
    <UploadImages
      :uploadMsg="uploadMsg"
      :max="max"
      :clearAll="clearAll"
      :fileError="fileError"
      @changed="handleImages"
    />
  </div>
</template>

<script>
import UploadImages from "vue-upload-drop-images";

export default {
  name: "UploadFile",
  components: {
    UploadImages,
  },
  props: {
    uploadMsg: String,
    clearAll: String,
    max: Number,
    handleImages: Function,
    fileError: String,
  },
};
</script>

<style scoped>
.upload-file .container {
  padding: 0;
  border: 1px dashed #a7aaae;
  background-color: #f6f6f7;
}
</style>

<style>
.imgsPreview {
  text-align: center;
}
.imgsPreview .imageHolder img {
  max-height: 100%;
  width: auto;
  height: auto;
}
.imgsPreview .imageHolder .plus,
.imgsPreview .imageHolder .delete {
  display: none;
}
.imgsPreview .imageHolder {
  background-color: transparent !important;
  width: auto;
  height: auto;
}
</style>
