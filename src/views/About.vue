<template>
  <div class="about">
    <div class="loading">
      <transition name="svg">
        <div class="loading_svg" v-if="temp">
          <lottie
            :options="defaultOptions"
            :speed="animationSpeed"
            :height="height"
            :width="width"
            v-on:animCreated="handleAnimation"
          />
        </div>
      </transition>
      <transition name="temp">
        <div class="loading_bg" v-if="temp">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
      </transition>
    </div>
    <div class="card" :style="{ background: BGColor(color.max) }">
      <transition name="card" mode="out-in">
        <div class="card_box" :class="color.max" v-if="view">
          <div class="card_box_inner">
            <div class="card_box_inner_res">
              <h2>
                あなたは<br />
                <span class="card_box_inner_res_key"
                  ><span :style="{ color: Color(color.max) }">{{
                    Word(color.max)
                  }}</span
                  >のような人です</span
                >
              </h2>
              <div class="card_box_inner_res_img">
                <div
                  class="card_box_inner_res_img_left"
                  :style="{ color: Color(color.max) }"
                >
                  {
                </div>
                <div class="card_box_inner_res_img_icon">
                  <v-lazy-image
                    :src="i"
                    alt=""
                    v-for="i in Icons(color.max)"
                    :key="i.id"
                  />
                </div>
                <p class="card_box_inner_res_img_and">&&</p>
                <div
                  class="card_box_inner_res_img_right"
                  :style="{ color: Color(color.max) }"
                >
                  }
                </div>
              </div>
              <h3 class="card_box_inner_res_h3">
                {{ h3(color.max) }}
              </h3>
              <p class="card_box_inner_res_descri">
                <span
                  v-for="t in descri(color.max)"
                  :class="subColor(color.max)"
                  :key="t.id"
                >
                  {{ t }}
                </span>
              </p>
            </div>
            <div class="card_box_inner_qr">
              <div class="card_box_inner_qr_img">
                <vue-qrcode
                  v-if="toLink"
                  :value="toLink"
                  tag="img"
                ></vue-qrcode>
              </div>
              <div class="card_box_inner_qr_word">
                <p>
                  Melikeギャラリーにカードを追加しよう!
                </p>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import * as firebase from "firebase/app";
import "firebase/database";
// import firebase from "firebase";
import Lottie from "../components/loader.vue";
// JSONデータを読み込み
import * as animationData from "../assets/loader.json";
import VueQrcode from "@chenfengyuan/vue-qrcode";
import { Howl } from "howler";
const sound = new Howl({
  src: "/src/sound/get.mp3",
  volume: 0.5
});

export default {
  components: {
    VueQrcode,
    Lottie
  },
  data() {
    return {
      color: false,
      view: false,
      list: [],
      left: true,
      right: false,
      height: 800,
      width: 800,
      svg: false,
      temp: false,
      card: false,
      defaultOptions: { animationData: animationData },
      animationSpeed: 1.7,
      n: 1,
      id: 0,
      bgcolor: "blue",
      toLink: "https://melike.netlify.com/",
      url: "https://melike.netlify.com/form"
    };
  },
  methods: {
    childAdded(snap) {
      this.temp = true;
      this.view = false;
      const li = snap.val();
      let max = this.maxNum(li.area);
      li.area[max.i] = 0;
      let max2 = this.maxNum(li.area);

      setTimeout(() => {
        this.temp = false;
        this.view = true;
        this.color = {
          max: li.list[max.i],
          max2: li.list[max2.i]
        };
        this.id = li.id;
        let para = "?color=" + this.color.max;
        let para2 = "&id=" + this.id;
        this.toLink = this.url + para + para2;
      }, 4200);
    },
    handleAnimation: function(anim) {
      this.anim = anim;
    },
    maxNum(l) {
      let index = 0;
      let value = 0;
      for (let i = 0; i < l.length; i++) {
        if (value < l[i]) {
          value = l[i];
          index = i;
        }
      }
      return { i: index, v: value };
    },
    resize() {
      this.height = window.innerWidth / 2;
      this.width = window.innerWidth / 2;
    }
  },
  mounted() {
    var db = firebase.database();
    db.ref("log")
      .limitToLast(1)
      .on("child_added", this.childAdded);
    this.height = window.innerWidth / 2;
    this.width = window.innerWidth / 2;
    window.addEventListener("resize", this.resize);
    sound.pkay();
  },
  computed: {
    Color() {
      return color => {
        switch (color) {
          case "red":
            return "#FF694B";
          case "orange":
            return "#FFBC55";
          case "lightblue":
            return "#1caee1";
          case "blue":
            return "#2283ad";
          case "yellow":
            return "#FED633";
          case "yellowgreen":
            return "#AAC864";
          case "green":
            return "#30a66a";
          case "violet":
            return "#A55B9A";
          case "pink":
            return "#EAA4D8";
          case "pinkvio":
            return "#DC659B";
          case "brown":
            return "#cd8256";
          case "black":
            return "#676767";
          case "rainbow":
            return "#FFBC55";
          default:
            return "#fff";
        }
      };
    },
    BGColor() {
      return color => {
        switch (color) {
          case "red":
            return "#FF694B";
          case "orange":
            return "#FFBC55";
          case "lightblue":
            return "#1caee1";
          case "blue":
            return "#2283ad";
          case "yellow":
            return "#FED633";
          case "yellowgreen":
            return "#AAC864";
          case "green":
            return "#30a66a";
          case "violet":
            return "#A55B9A";
          case "pink":
            return "#EAA4D8";
          case "pinkvio":
            return "#DC659B";
          case "brown":
            return "#cd8256";
          case "black":
            return "#676767";
          case "rainbow":
            return "linear-gradient(-45deg,#FF694B,#FFBC55,#FED633,#30a66a,#1caee1,#2283ad,#DC659B)";
          default:
            return "#fff";
        }
      };
    },
    subColor() {
      return color => {
        switch (color) {
          case "red":
            return "brown";
          case "orange":
            return "green";
          case "lightblue":
            return "green";
          case "blue":
            return "yellowgreen";
          case "yellow":
            return "lightblue";
          case "yellowgreen":
            return "red";
          case "green":
            return "red";
          case "violet":
            return "pink";
          case "pink":
            return "lightblue";
          case "pinkvio":
            return "brown";
          case "brown":
            return "yellow";
          case "black":
            return "red";
          case "rainbow":
            return "orange";
          default:
            return "red";
        }
      };
    },
    Word() {
      return color => {
        switch (color) {
          case "red":
            return "真っ赤に燃える炎";
          case "orange":
            return "明るく照らしている太陽";
          case "lightblue":
            return "周囲を働きかける雨";
          case "blue":
            return "環境に潤いを与える水";
          case "yellow":
            return "光を目指し続けるひまわり";
          case "yellowgreen":
            return "優しさ溢れるクローバー";
          case "green":
            return "実をつけ成長し続ける木";
          case "violet":
            return "自由にはばたく蝶々";
          case "pink":
            return "しなやかに舞う桜";
          case "pinkvio":
            return "自由にはばたく蝶々";
          case "brown":
            return "広い心を持った大地";
          case "black":
            return "環境をきれいにする炭";
          case "rainbow":
            return "希望や未来を与える虹";
          default:
            return "環境をきれいにする炭";
        }
      };
    },
    h3() {
      return color => {
        switch (color) {
          case "red":
            return "「情熱、活力、勝利」といった強いエネルギーを大切にしている人。";
          case "orange":
            return "「喜び、共創、元気」といった共感を大切にしている人。";
          case "lightblue":
            return "「誠実、純粋、信頼」といった人情の厚い人。";
          case "blue":
            return "「信頼、爽やか、開放感」といった包容力のある人。";
          case "yellow":
            return "「歓喜、前進、無邪気」といった努力し続ける人。";
          case "yellowgreen":
            return "「癒し、優しさ、平和」といった調和を大切にしている人。";
          case "green":
            return "「成長、癒し、生命力」といった環境大切にしている人。";
          case "violet":
            return "「優雅、芸術、神秘」といったエレガントで繊細な人。";
          case "pink":
            return "「優しさ、開放感、成長」といった思いやりを大切にしている人。";
          case "pinkvio":
            return "「優雅、芸術、神秘」といったエレガントで繊細な人。";
          case "brown":
            return "「温もり、のどか、追及」と無限の可能性を秘めている人。";
          case "black":
            return "「深い、未知、高級」といった強いエネルギーを大切にしている人。";
          case "rainbow":
            return "「夢、幸運、吸収」といった輝きを大切にしている人。";
          default:
            return "「深い、未知、高級」といった強いエネルギーを大切にしている人。";
        }
      };
    },
    descri() {
      return color => {
        switch (color) {
          case "red":
            return [
              "火が燃えたら灰(土)が残るように、広い心を持った",
              "「大地」",
              "の人と一緒だと良いお仕事につながるかも"
            ];
          case "orange":
            return [
              "太陽のエネルギーで植物が育ち緑が生い茂るように",
              "「木」",
              "の人と一緒だと自分をの力を発揮し続けるかも"
            ];
          case "lightblue":
            return [
              "雨が降ったら、木などの植物が育つように",
              "「木」",
              "の人と一緒だと自ら働きかける力が生まれてよい成果が出せるかも"
            ];
          case "blue":
            return [
              "命あるものすべてに成長する力を与える水のように",
              "「植物」",
              "自分の力が誰かに良い影響を与え誰かのためになるかも"
            ];
          case "yellow":
            return [
              "植物は雨を吸収し、自分の力として成長し続けるように",
              "「雨」",
              "の人と一緒だとその人の良いところを掴み自分の力に変えていけるかも"
            ];
          case "yellowgreen":
            return [
              "クローバーは炎の火種になるように、熱い情熱を持った",
              "「炎」",
              "の人と一緒だとよいお仕事につながるかも"
            ];
          case "green":
            return [
              "クローバーは炎の火種になるように、熱い情熱を持った",
              "「炎」",
              "の人と一緒だとよいお仕事につながるかも"
            ];
          case "violet":
            return [
              "植物に花粉を運ぶように美しくきれいな",
              "「花」",
              "の人と一緒だと幸福をもたらしてくれるかも"
            ];
          case "pink":
            return [
              "雨を吸収してどんどん成長して大きくなるように、植物に栄養を与える",
              "「雨」",
              "の人と一緒だと自分を常に進化し続けられるかも"
            ];
          case "pinkvio":
            return [
              "植物に花粉を運ぶように美しくきれいな",
              "「花」",
              "の人と一緒だと幸福をもたらしてくれるかも"
            ];
          case "brown":
            return [
              "大地から金が採掘されるように",
              "「金」",
              "の人と一緒だと自分の新たな発見をし無限に成長できるかも"
            ];
          case "black":
            return [
              "炭で火の燃やせる可能性が広がるように",
              "「火」",
              "の人と一緒だとパワーを発揮できるかも。さらに、土や空気の環境もきれいに浄化するよ"
            ];
          case "rainbow":
            return [
              "太陽の光によって虹が発生するように、輝きを放つ",
              "「太陽」",
              "の人と一緒にいると未来の懸け橋につながるかも"
            ];
          default:
            return [
              "炭で火の燃やせる可能性が広がるように",
              "「火」",
              "の人と一緒だとパワーを発揮できるかも。さらに、土や空気の環境もきれいに浄化するよ"
            ];
        }
      };
    },
    Icons() {
      return color => {
        switch (color) {
          case "red":
            return ["/src/img/icons/fire.png", "/src/img/icons/bud.png"];
          case "orange":
            return ["/src/img/icons/sun.png", "/src/img/icons/wood.png"];
          case "lightblue":
            return ["/src/img/icons/rain.png", "/src/img/icons/wood.png"];
          case "blue":
            return ["/src/img/icons/water.png", "/src/img/icons/clover.png"];
          case "yellow":
            return ["/src/img/icons/sunflower.png", "/src/img/icons/water.png"];
          case "yellowgreen":
            return ["/src/img/icons/clover.png", "/src/img/icons/fire.png"];
          case "green":
            return ["/src/img/icons/wood.png", "/src/img/icons/fire.png"];
          case "violet":
            return ["/src/img/icons/fly.png", "/src/img/icons/bud.png"];
          case "pink":
            return ["/src/img/icons/blossom.png", "/src/img/icons/rain.png"];
          case "pinkvio":
            return ["/src/img/icons/fly.png", "/src/img/icons/bud.png"];
          case "brown":
            return ["/src/img/icons/hill.png", "/src/img/icons/gold.png"];
          case "black":
            return ["/src/img/icons/charcoal.png", "/src/img/icons/fire.png"];
          case "rainbow":
            return ["/src/img/icons/rainbow.png", "/src/img/icons/sun.png"];
          default:
            return ["/src/img/icons/charcoal.png", "/src/img/icons/fire.png"];
        }
      };
    }
  }
};
</script>

<style lang="scss">
.about {
  height: 100%;
  width: 100%;
  overflow: hidden;
  background: #faf7d9;
  position: relative;
  .loading {
    height: 100%;
    width: 100%;
    position: relative;
    &_svg {
      height: 100%;
      width: 100%;
      position: absolute;
      display: flex;
      justify-content: center;
      align-items: center;
      top: 0;
      left: 0;
      z-index: 5;
    }
    &_bg {
      height: 100%;
      width: 100%;
      position: absolute;
      top: 0;
      left: 0;
      display: flex;
      z-index: 3;
      span {
        display: block;
        height: 0%;
        width: 25%;
        background: #ffd502;
        animation: h-100 0.7s ease-in both;
        &:nth-child(1) {
          animation-delay: 0.1s;
        }
        &:nth-child(2) {
          animation-delay: 0.3s;
        }
        &:nth-child(3) {
          animation-delay: 0.5s;
        }
        &:nth-child(4) {
          animation-delay: 0.7s;
        }
      }
    }
  }
  .card {
    height: 100%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 2;
    display: flex;
    justify-items: center;
    align-items: center;
    &_box {
      height: calc(100% - 6vw);
      width: calc(100% - 6vw);
      margin: 0 auto;
      position: relative;
      display: flex;
      justify-items: center;
      align-items: center;
      overflow: hidden;
      &::before,
      &::after {
        content: "";
        position: absolute;
      }

      &::before {
        height: 100%;
        width: 0;
        top: 0;
        left: 0;
        background: #fff;
        animation: w-100 0.4s ease-in 0.7s both;
      }

      &.red {
        &::after {
          background: url("../assets/img/bg/red.png") center center repeat;
        }
      }
      &.orange {
        &::after {
          background: url("../assets/img/bg/orange.png") center center repeat;
        }
      }
      &.lightblue {
        &::after {
          background: url("../assets/img/bg/lightblue.png") center center repeat;
        }
      }
      &.blue {
        &::after {
          background: url("../assets/img/bg/blue.png") center center repeat;
        }
      }
      &.yellow {
        &::after {
          background: url("../assets/img/bg/yellow.png") center center repeat;
        }
      }
      &.yellowgreen {
        &::after {
          background: url("../assets/img/bg/yellowgreen.png") center center
            repeat;
        }
      }
      &.green {
        &::after {
          background: url("../assets/img/bg/green.png") center center repeat;
        }
      }
      &.violet {
        &::after {
          background: url("../assets/img/bg/violet.png") center center repeat;
        }
      }
      &.pink {
        &::after {
          background: url("../assets/img/bg/pink.png") center center repeat;
        }
      }
      &.pinkvio {
        &::after {
          background: url("../assets/img/bg/pinkvio.png") center center repeat;
        }
      }
      &.brown {
        &::after {
          background: url("../assets/img/bg/brown.png") center center repeat;
        }
      }
      &.black {
        &::after {
          background: url("../assets/img/bg/brown.png") center center repeat;
        }
      }
      &.rainbow {
        &::after {
          background: url("../assets/img/bg/red.png") center center repeat;
        }
      }
      &::after {
        height: 300%;
        width: 300%;
        top: -100%;
        left: -100%;
        background-size: 7vw !important;
        transform: rotate(45deg);
        z-index: 1;
        opacity: 0.5;
        animation: o-05 0.4s ease-in 0.7s both;
      }
      &_inner {
        height: calc(100% - 8vw);
        width: calc(100% - 8vw);
        margin: 0 auto;
        position: relative;
        display: grid;
        grid-template-columns: 13fr 7fr;
        &::after {
          content: "";
          position: absolute;
          height: 100%;
          width: 100%;
          top: 0;
          right: 0;
          background: #fff;
          animation: w-100 0.4s ease-in 1.1s both;
          z-index: 3;
        }
        &_res {
          display: flex;
          flex-wrap: wrap;
          justify-content: center;
          align-content: center;
          width: 80%;
          margin: 0 auto;
          position: relative;
          z-index: 4;
          h2 {
            font-size: 1.3vw;
            display: inline-block;
            line-height: 1.4;
            width: 100%;
            margin: 0 auto;
            animation: o-1 0.4s ease-in 1.7s both;
          }
          &_key {
            font-size: 1.5vw;
            font-family: "yasasi b";
            font-weight: 700;
            span {
              font-size: 200%;
              margin-right: 2%;
            }
          }
          &_img {
            width: 100%;
            height: 10vw;
            margin-top: 1.5vw;
            position: relative;
            animation: o-1 0.4s ease-in 1.8s both;

            &_left,
            &_right {
              position: absolute;
              top: 50%;
              transform: translateY(-50%);
              font-size: 5vw;

              font-weight: 700;
            }
            &_left {
              left: 0;
            }
            &_right {
              right: 0;
            }
            &_icon {
              height: 100%;
              width: 100%;
              position: relative;
              img {
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                &:nth-child(1) {
                  height: 90%;
                  left: 14%;
                }
                &:nth-child(2) {
                  height: 60%;
                  right: 14%;
                }
              }
            }
            &_and {
              position: absolute;
              top: 50%;
              left: 50%;
              transform: translate(-50%, -50%);
              font-size: 2.5vw;
              font-family: "yasasi b";
              font-weight: 700;
            }
          }
          &_h3 {
            font-size: 1.5vw;
            font-family: "yasasi b";
            font-weight: 700;
            width: 100%;
            line-height: 1.4;
            margin-top: 3vw;
            animation: o-1 0.4s ease-in 1.9s both;
          }
          &_descri {
            margin-top: 1vw;
            font-size: 1.3vw;
            line-height: 1.4;
            animation: o-1 0.4s ease-in 2s both;
            .red {
              &:nth-child(2) {
                color: #ff694b;
              }
            }
            .orange {
              &:nth-child(2) {
                color: #ffbc55;
              }
            }
            .lightblue {
              &:nth-child(2) {
                color: #1caee1;
              }
            }
            .blue {
              &:nth-child(2) {
                color: #2283ad;
              }
            }
            .yellow {
              &:nth-child(2) {
                color: #fed633;
              }
            }
            .yellowgreen {
              &:nth-child(2) {
                color: #aac864;
              }
            }
            .green {
              &:nth-child(2) {
                color: #30a66a;
              }
            }
            .violet {
              &:nth-child(2) {
                color: #a55b9a;
              }
            }
            .pink {
              &:nth-child(2) {
                color: #eaa4d8;
              }
            }
            .pinkvio {
              &:nth-child(2) {
                color: #dc659b;
              }
            }
            .brown {
              &:nth-child(2) {
                color: #cd8256;
              }
            }
            span {
              &:nth-child(2) {
                font-family: "yasasi b";
                font-weight: 700;
              }
            }
          }
        }
        &_qr {
          // background: #ccc;
          display: grid;
          grid-gap: 20px;
          justify-items: center;
          align-content: center;
          position: relative;
          z-index: 4;
          font-size: 1.3vw;
          animation: o-1 0.4s ease-in 2.1s both;
          &_img {
            width: 50%;
            img {
              width: 100%;
            }
          }
        }
      }
    }
  }
}
.about {
  .svg-enter {
    transform: translateY(-150px);
    opacity: 0;
  }
  .svg-enter-active {
    transition: all 0.6s 1.2s;
  }
  .svg-enter-to {
    opacity: 1;
  }
  .svg-leave-active {
    transition: all 0.7s;
  }
  .svg-leave-to {
    transform: translateY(-100%);
  }
  .temp-leave-active {
    transition: all 0.7s;
  }
  .temp-leave-to {
    transform: translateY(-100%);
  }
  .card-leave-active {
    transition: all 0.7s 2s;
  }
  .card-leave-to {
    transform: translateY(-100%);
  }
}
@keyframes h-100 {
  from {
    height: 0%;
  }
  40% {
    height: 95%;
  }
  80% {
    height: 97.5%;
  }
  20%,
  60%,
  to {
    height: 100%;
  }
}
@keyframes w-100 {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}
@keyframes o-05 {
  from {
    opacity: 0;
  }
  to {
    opacity: 0.5;
  }
}
@keyframes o-1 {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@keyframes b-scale {
  from {
    transform: scale(0);
  }
  40% {
    transform: scale(1.02);
  }
  80% {
    transform: scale(1.05);
  }
  20%,
  60%,
  to {
    transform: scale(1);
  }
}
@keyframes s-1 {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}
</style>
