<template>
  <div id="app">
    <mdb-container class="mt-5">
    <mdb-row>
      <GalleryComponent
        v-for="image in imageNameList"
        :key="image.id"
        :imageName="image"
        />
    </mdb-row>
  </mdb-container>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import GalleryComponent from './components/GalleryComponent.vue'
import {
  mdbContainer,
  mdbRow
} from "mdbvue";
const axios = require('axios').default;

export default {
  name: 'App',
  components: {
    // HelloWorld,
    GalleryComponent,
    mdbContainer,
    mdbRow
  },
  data: function() {
    return {
      imageNameList: [],
      images: [
      ]
    }
  },
  methods: {
    getImageList() {
      const path = 'http://localhost:5000/images/list';
      axios.get(path)
        .then((res) => {
          this.imageNameList = res.data
          console.log(this.imageNameList)
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getAllImages() {
      var imageName = ''
      for (imageName of this.imageNameList) {
        var image = {
          image: '',
          metadata: ''
        }
        image.image = this.getImage(imageName)
        image.metadata = this.getMetaData(imageName)
        this.images.append(image)
      }
    },
    getImage(name) {
      const path = 'http://localhost:5000/images/' + name;
      axios.get(path)
        .then((res) => {
          return res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getImageMetadata(name) {
      const path = 'http://localhost:5000/images/metadata/' + name;
      axios.get(path)
      .then((res) => {
        return res.data
      })
      .catch((error) => {
        console.error(error);
      })
    }
  },
  created() {
    this.getImageList();
    this.getAllImages();
  },
}
</script>

<style lang="scss">
$image-path: '~@/../mdb/mdbvue/img';
@import '~@/../mdb/mdbvue/scss/mdb-free.scss';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
