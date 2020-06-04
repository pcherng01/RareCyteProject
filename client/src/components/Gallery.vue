<template>
  <mdb-container class="mt-5">
    <mdb-row>
      <!-- Grid column -->
      <mdb-col lg="4" md="12" class="mb-4">
        <a @click="showModal = true"><img class="img-fluid z-depth-1" src="../../../resources/images/PIA04216_orig.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal" @close="showModal = false">
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>

      <!-- Grid column -->
      <!-- Grid column -->
      <mdb-col lg="4" md="6" class="mb-4">
        <a @click="showModal2 = true"><img class="img-fluid z-depth-1" src="../../../resources/images/GSFC_20171208_Archive_e001465_orig.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal2" @close="showModal2 = false">
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal2 = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
      <!-- Grid column -->
      <!-- Grid column -->
      <mdb-col lg="4" md="6" class="mb-4">
        <a @click="showModal3 = true"><img class="img-fluid z-depth-1" src="../../../resources/images/PIA04215_orig.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal3" @close="showModal3 = false">
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal3 = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
      <!-- Grid column -->
      <!-- Grid column -->
      <mdb-col lg="4" md="6" class="mb-4">
        <a @click="showModal4 = true"><img class="img-fluid z-depth-1" src="../../../resources/images/hubble-sees-the-wings-of-a-butterfly-the-twin-jet-nebula_20283986193_o_orig.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal4" @close="showModal4 = false">
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal4 = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
      <!-- Grid column -->
      <!-- Grid column -->
      <!-- Grid column -->
      <!-- Grid column -->
      <!-- Grid column -->
    </mdb-row>
  </mdb-container>
</template>

<script>
  // const axios = require('axios').default;
  var imageList = [];
  import { mdbContainer,
    mdbRow,
    mdbCol,
    // mdbIcon,
    mdbBtn,
    // mdbLightbox,
    // mdbCarousel,
    // mdbCard,
    mdbModal,
    // mdbModalHeader,
    // mdbModalTitle,
    // mdbModalBody,
    mdbModalFooter,
    // mdbNavItem
  } from "mdbvue";
  export default {
    name: "GalleryPage",
    data: function () {
      return {
        count: 0,
          imageList: [{}],
          showModal: false,
          showModal2: false,
          showModal3: false,
          showModal4: false,
          showModal5: false,
          showModal6: false
      }
    },
    methods: {
      getMessage() {
        const path = 'http://localhost:5000/images/list';
        axios.get(path)
          .then((res) => {
            // console.log(res.data)
            this.imageList = res.data
            console.log(this.imageList)
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
    },
    created() {
      this.getMessage();
    },
    components: {
      mdbContainer,
      mdbRow,
      mdbCol,
      // mdbIcon,
      mdbBtn,
      // mdbLightbox,
      // mdbCarousel,
      // mdbCard,
      mdbModal,
      // mdbModalHeader,
      // mdbModalTitle,
      // mdbModalBody,
      mdbModalFooter,
      // mdbNavItem
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @media (min-width: 768px) {
    .carousel-multi-item-2 .col-md-3 {
      float: left;
      width: 25%;
      max-width: 100%; } }

    .carousel-multi-item-2 .card img {
      border-radius: 2px; }

    figure {
      cursor: pointer;
    }
</style>
