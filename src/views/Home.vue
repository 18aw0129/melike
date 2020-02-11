<template>
  <div class="home">
    <main class="canvas">
      <div class="canvas_inner">
        <div class="canvas_inner_image">
          <v-lazy-image :src="img" v-for="img in images" :key="img.id" />
        </div>
        <div class="canvas_inner_cards" v-show="load">
          <transition-group tag="ul" name="up" appear mode="out-in">
            <div class="card" v-for="card in cards" :key="card.key" ref="card">
              <div class="card_bg" :style="{ background: BGColor(card.color) }">
                <div class="card_bg_inner" :class="card.color">
                  <div class="res">
                    <h2>
                      {{ card.job }}{{ card.year }}年目のあなたは
                      <span class="res_key"
                        ><span :style="{ color: Color(card.color) }">{{
                          Word(card.color)
                        }}</span>
                        のような人です
                      </span>
                    </h2>
                    <div class="res_img">
                      <div
                        class="res_img_left"
                        :style="{ color: Color(card.color) }"
                      >
                        {
                      </div>
                      <div class="res_img_icon">
                        <img
                          :src="i"
                          alt=""
                          v-for="i in Icons(card.color)"
                          :key="i.id"
                        />
                      </div>
                      <p class="res_img_and">&&</p>
                      <div
                        class="res_img_right"
                        :style="{ color: Color(card.color) }"
                      >
                        }
                      </div>
                    </div>
                    <h3 class="res_h3">
                      {{ h3(card.color) }}
                    </h3>
                    <p class="res_descri">
                      <span
                        v-for="t in descri(card.color)"
                        :class="subColor(card.color)"
                        :key="t.id"
                      >
                        {{ t }}
                      </span>
                    </p>
                  </div>
                  <div class="req">
                    <div
                      class="req_logo"
                      :style="{ background: BGColor(subColor(card.color)) }"
                    >
                      <img :src="Icon(card.color)" alt="" />
                    </div>
                    <div class="req_fm">
                      <div
                        class="req_fm_now"
                        :style="{ background: BGColor(card.color) }"
                      >
                        <span
                          class="head"
                          :style="{ background: BGColor(card.color) }"
                          >今</span
                        >
                        <p>大切にしていること</p>
                        <div
                          class="line"
                          :style="{ background: BGColor(card.color) }"
                        ></div>
                        <p :style="{ color: Color(card.color) }">
                          {{ card.now }}
                        </p>
                      </div>
                      <div
                        class="req_fm_future"
                        :style="{ background: BGColor(card.color) }"
                      >
                        <span
                          class="head"
                          :style="{ background: BGColor(card.color) }"
                          >未来</span
                        >
                        <p>大事にしたいこと</p>
                        <div
                          class="line"
                          :style="{ background: BGColor(card.color) }"
                        ></div>
                        <p :style="{ color: Color(card.color) }">
                          {{ card.future }}
                        </p>
                      </div>
                    </div>
                    <div class="req_fm_img">
                      <img :src="'data:image/jpeg;base64,' + card.url" alt="" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </transition-group>
        </div>
        <transition name="pop" mode="out-in">
          <div class="canvas_inner_pop" v-if="pop">
            <div class="card">
              <div class="card_bg" :style="{ background: BGColor(card.color) }">
                <div class="card_bg_inner" :class="card.color">
                  <div class="res">
                    <h2>
                      {{ card.job }}{{ card.year }}年目のあなたは
                      <span class="res_key"
                        ><span :style="{ color: Color(card.color) }">{{
                          Word(card.color)
                        }}</span>
                        のような人です
                      </span>
                    </h2>
                    <div class="res_img">
                      <div
                        class="res_img_left"
                        :style="{ color: Color(card.color) }"
                      >
                        {
                      </div>
                      <div class="res_img_icon">
                        <v-lazy-image
                          :src="i"
                          alt=""
                          v-for="i in Icons(card.color)"
                          :key="i.id"
                        />
                      </div>
                      <p class="res_img_and">&&</p>
                      <div
                        class="res_img_right"
                        :style="{ color: Color(card.color) }"
                      >
                        }
                      </div>
                    </div>
                    <h3 class="res_h3">
                      {{ h3(card.color) }}
                    </h3>
                    <p class="res_descri">
                      <span
                        v-for="t in descri(card.color)"
                        :class="subColor(card.color)"
                        :key="t.id"
                      >
                        {{ t }}
                      </span>
                    </p>
                  </div>
                  <div class="req">
                    <div
                      class="req_logo"
                      :style="{ background: BGColor(subColor(card.color)) }"
                    >
                      <img :src="Icon(card.color)" alt="" />
                    </div>
                    <div class="req_fm">
                      <div
                        class="req_fm_now"
                        :style="{ background: BGColor(card.color) }"
                      >
                        <span
                          class="head"
                          :style="{ background: BGColor(card.color) }"
                          >今</span
                        >
                        <p>大切にしていること</p>
                        <div
                          class="line"
                          :style="{ background: BGColor(card.color) }"
                        ></div>
                        <p :style="{ color: Color(card.color) }">
                          {{ card.now }}
                        </p>
                      </div>
                      <div
                        class="req_fm_future"
                        :style="{ background: BGColor(card.color) }"
                      >
                        <span
                          class="head"
                          :style="{ background: BGColor(card.color) }"
                          >未来</span
                        >
                        <p>大事にしたいこと</p>
                        <div
                          class="line"
                          :style="{ background: BGColor(card.color) }"
                        ></div>
                        <p :style="{ color: Color(card.color) }">
                          {{ card.future }}
                        </p>
                      </div>
                    </div>
                    <div class="req_fm_img">
                      <v-lazy-image
                        :src="'data:image/jpeg;base64,' + card.url"
                        alt=""
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </transition>
        <h1 class="canvas_inner_title">Melike</h1>
      </div>
    </main>
  </div>
</template>

<script>
import * as firebase from "firebase/app";
import "firebase/database";
import { TweenMax } from "gsap";
import { Howl } from "howler";
const sound = new Howl({
  src: "/src/sound/get.mp3",
  volume: 0.5
});
export default {
  name: "home",
  data() {
    return {
      images: [
        require("@/assets/img/earth_in.png"),
        require("@/assets/img/earth_out.png")
      ],
      cards: [],
      load: false,
      num: 0,
      time: null,
      pop: false,
      card: {},
      speed: 0,
      set: true
    };
  },
  methods: {
    getRadian(angle) {
      return ((Math.PI * 2) / this.cards.length) * angle;
    },
    loop() {
      for (let i = 0; i < this.cards.length; i++) {
        let radian = this.getRadian(i);
        let offsetX = Math.cos(radian + this.speed);
        let offsetY = Math.sin(radian + this.speed);
        if (offsetY >= 0.7) {
          TweenMax.set(this.$refs.card[i], {
            x: offsetX * -60 + "vw",
            y: offsetY * -60 + "vw",
            scale: offsetY + 0.3
          });
        } else {
          TweenMax.set(this.$refs.card[i], {
            x: offsetX * -60 + "vw",
            y: offsetY * -60 + "vw",
            scale: 1
          });
        }
      }

      this.speed += 0.001;
      requestAnimationFrame(() => {
        this.loop();
      });
    },
    childAdded(snap) {
      let data = snap.val();
      firebase
        .database()
        .ref("url")
        .child(data.id)
        .once("value", s => {
          this.pop = true;
          let url = s.val().url;
          if (this.num > 9) {
            this.cards.splice(this.num % 10, 1, {
              key: data.uniq,
              id: data.id,
              color: data.color,
              url: url,
              job: data.job,
              year: data.year,
              now: data.now,
              future: data.future
            });
            sound.play();
          } else {
            this.cards.push({
              key: data.uniq,
              id: data.id,
              color: data.color,
              url: url,
              job: data.job,
              year: data.year,
              now: data.now,
              future: data.future
            });
          }
          this.card = {
            key: data.uniq,
            id: data.id,
            color: data.color,
            url: url,
            job: data.job,
            year: data.year,
            now: data.now,
            future: data.future
          };
        })
        .then(() => {
          this.num++;
        });
      if (this.set) {
        this.loop();
        this.set = false;
      }
    }
  },
  created() {
    firebase
      .database()
      .ref("view")
      .limitToLast(10)
      .on("child_added", this.childAdded);
  },
  mounted() {
    this.load = true;
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
    },
    Icon() {
      return color => {
        switch (color) {
          case "red":
            return "/src/img/icons/fire.png";
          case "orange":
            return "/src/img/icons/sun.png";
          case "lightblue":
            return "/src/img/icons/rain.png";
          case "blue":
            return "/src/img/icons/water.png";
          case "yellow":
            return "/src/img/icons/sunflower.png";
          case "yellowgreen":
            return "/src/img/icons/clover.png";
          case "green":
            return "/src/img/icons/wood.png";
          case "violet":
            return "/src/img/icons/fly.png";
          case "pink":
            return "/src/img/icons/blossom.png";
          case "pinkvio":
            return "/src/img/icons/fly.png";
          case "brown":
            return "/src/img/icons/hill.png";
          case "black":
            return "/src/img/icons/charcoal.png";
          case "rainbow":
            return "/src/img/icons/rainbow.png";
          default:
            return "/src/img/icons/charcoal.png";
        }
      };
    }
  },
  watch: {
    pop(n) {
      if (n) {
        setTimeout(() => {
          this.pop = false;
        }, 8000);
      }
    }
  }
};
</script>

<style lang="scss">
.home {
  height: 100%;
  width: 100%;
  overflow: hidden;
  background: #faf7d9;
  position: relative;
  .canvas {
    position: absolute;
    height: 100%;
    width: 100%;
    &_inner {
      position: relative;
      height: 100%;
      width: 100%;
      &_image {
        position: absolute;
        height: 100%;
        width: 100%;
        bottom: -50%;
        img {
          position: absolute;
          height: 100%;
          width: 100%;
          top: 0;
          left: 0;
          object-fit: contain;
          animation: bIn 0.6s ease-in 0.3s backwards;
          &:nth-child(2) {
            animation: r-360 45s linear infinite;
          }
        }
      }
      &_cards {
        position: absolute;
        height: 100%;
        width: 100%;
        top: 0;
        left: 0;
        ul {
          position: absolute;
          height: 100%;
          width: 100%;
          top: 0;
          left: 0;
        }
        .card {
          position: absolute;
          height: 14.4vw;
          width: 25.6vw;
          bottom: -27vw;
          left: calc(50% - 12.8vw);
          transform-origin: center center;
          &_bg {
            height: 100%;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            animation: bIn 0.6s ease-in 0.3s backwards;
            &_inner {
              position: relative;
              height: calc(100% - 1vw);
              width: calc(100% - 1vw);
              background: #fff;
              overflow: hidden;
              display: grid;
              grid-template-columns: 7fr 3fr;
              .res {
                position: relative;
                z-index: 1;
                background: #fff;
                margin: 0.5vw;
                h2 {
                  font-size: 0.6vw;
                  margin: 10% 5% 0;
                }
                &_key {
                  margin-top: 2%;
                  display: inline-block;
                  span {
                    font-size: 0.8vw;
                    font-family: "yasasi b";
                  }
                }
                &_img {
                  width: 80%;
                  height: 28%;
                  position: relative;
                  margin: 2% auto 0;
                  &_left,
                  &_right {
                    position: absolute;
                    top: 50%;
                    transform: translateY(-50%);
                    font-size: 1.5vw;
                    font-family: "yasasi b";
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
                        height: 100%;
                        left: 10%;
                      }
                      &:nth-child(2) {
                        height: 50%;
                        right: 14%;
                      }
                    }
                  }
                  &_and {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    font-size: 0.8vw;
                    font-family: "yasasi b";
                    font-weight: 700;
                  }
                }
                &_h3 {
                  font-size: 0.5vw;
                  width: 100%;
                  margin: 0 5%;
                  line-height: 1.4;
                  font-family: "yasasi b";
                  margin-top: 3%;
                }
                &_descri {
                  margin-top: 1%;
                  margin: 2% 5% 0;
                  font-size: 0.5vw;
                  line-height: 1.4;
                  span {
                    &:nth-of-type(2) {
                      display: inline-block;
                    }
                  }
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
              .req {
                position: relative;
                z-index: 2;
                &_logo {
                  position: absolute;
                  height: 3vw;
                  width: 3vw;
                  right: 0.5vw;
                  top: 0.5vw;
                  border-radius: 0.5vw;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  img {
                    height: 80%;
                  }
                  &:after {
                    content: "";
                    position: absolute;
                    height: 80%;
                    width: 80%;
                    border: solid #fff 0.1vw;
                    border-radius: 0.3vw;
                  }
                }
                &_fm {
                  position: absolute;
                  z-index: 1;
                  font-size: 0.6vw;
                  bottom: 24%;
                  right: 0.7vw;
                  width: 75%;
                  font-family: "yasasi b";
                  &_now {
                    position: relative;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    align-items: center;
                    width: 100%;
                    height: 2.3vw;
                    padding: 0.1vw;
                    .head {
                      position: absolute;
                      z-index: 3;
                      height: 1.6vw;
                      width: 1.6vw;
                      text-align: center;
                      line-height: 1.6vw;
                      border-radius: 50%;
                      left: -0.8vw;
                      top: -0.5vw;
                      color: #fff;
                      font-family: "yasasi b";
                    }
                    &:after {
                      content: "";
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      height: calc(100% - 0.3vw);
                      width: calc(100% - 0.3vw);
                      transform: translate(-50%, -50%);
                      background: #fff;
                    }
                    p {
                      position: relative;
                      z-index: 3;
                      width: 100%;
                      text-align: center;
                      font-size: 0.6vw;
                      line-height: 1.1vw;
                      white-space: nowrap;
                      &:nth-of-type(1) {
                        font-size: 0.4vw;
                      }
                    }
                    .line {
                      width: 80%;
                      height: 4%;
                      z-index: 4;
                    }
                  }
                  &_future {
                    position: relative;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    align-items: center;
                    width: 100%;
                    height: 2.3vw;
                    padding: 0.1vw;
                    margin-top: 10%;
                    .head {
                      position: absolute;
                      z-index: 3;
                      height: 1.6vw;
                      width: 1.6vw;
                      text-align: center;
                      line-height: 1.6vw;
                      border-radius: 50%;
                      left: -0.8vw;
                      top: -0.5vw;
                      color: #fff;
                    }
                    &:after {
                      content: "";
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      height: calc(100% - 0.3vw);
                      width: calc(100% - 0.3vw);
                      transform: translate(-50%, -50%);
                      background: #fff;
                    }
                    p {
                      position: relative;
                      width: 100%;
                      text-align: center;
                      z-index: 3;
                      font-size: 0.6vw;
                      line-height: 1.1vw;
                      white-space: nowrap;
                      &:nth-of-type(1) {
                        font-size: 0.4vw;
                      }
                    }
                    .line {
                      width: 80%;
                      height: 4%;
                      z-index: 4;
                    }
                  }
                  &_img {
                    position: absolute;
                    right: 0.5vw;
                    bottom: 2%;
                    height: 15%;
                    img {
                      height: 100%;
                    }
                  }
                }
              }
              &.red {
                &::after {
                  background: url("../assets/img/bg/red.png") center center
                    repeat;
                }
              }
              &.orange {
                &::after {
                  background: url("../assets/img/bg/orange.png") center center
                    repeat;
                }
              }
              &.lightblue {
                &::after {
                  background: url("../assets/img/bg/lightblue.png") center
                    center repeat;
                }
              }
              &.blue {
                &::after {
                  background: url("../assets/img/bg/blue.png") center center
                    repeat;
                }
              }
              &.yellow {
                &::after {
                  background: url("../assets/img/bg/yellow.png") center center
                    repeat;
                }
              }
              &.yellowgreen {
                &::after {
                  background: url("../assets/img/bg/yellowgreen.png") center
                    center repeat;
                }
              }
              &.green {
                &::after {
                  background: url("../assets/img/bg/green.png") center center
                    repeat;
                }
              }
              &.violet {
                &::after {
                  background: url("../assets/img/bg/violet.png") center center
                    repeat;
                }
              }
              &.pink {
                &::after {
                  background: url("../assets/img/bg/pink.png") center center
                    repeat;
                }
              }
              &.pinkvio {
                &::after {
                  background: url("../assets/img/bg/pinkvio.png") center center
                    repeat;
                }
              }
              &.brown {
                &::after {
                  background: url("../assets/img/bg/brown.png") center center
                    repeat;
                }
              }
              &.black {
                &::after {
                  background: url("../assets/img/bg/brown.png") center center
                    repeat;
                }
              }
              &.rainbow {
                &::after {
                  background: url("../assets/img/bg/red.png") center center
                    repeat;
                }
              }
              &::after {
                content: "";
                position: absolute;
                height: 300%;
                width: 300%;
                top: -100%;
                left: -100%;
                background-size: 3vw !important;
                opacity: 0.5;
                transform: rotate(45deg);
                touch-action: none;
              }
            }
          }
        }
      }
      &_pop {
        position: absolute;
        height: 100%;
        width: 100%;
        .card {
          position: absolute;
          height: 14.4vw;
          width: 25.6vw;
          bottom: calc(50% - 7.2vw);
          left: calc(50% - 12.8vw);
          transform-origin: center center;
          animation: bInD 0.6s ease-in 0.3s backwards;
          &_bg {
            height: 100%;
            width: 100%;
            display: flex;
            transform: scale(1.8);
            transform-origin: center center;
            justify-content: center;
            align-items: center;
            box-shadow: 0 0 1vw rgba(0, 0, 0, 0.4);
            &_inner {
              position: relative;
              height: calc(100% - 1vw);
              width: calc(100% - 1vw);
              background: #fff;
              overflow: hidden;
              display: grid;
              grid-template-columns: 7fr 3fr;
              .res {
                position: relative;
                z-index: 1;
                background: #fff;
                margin: 0.5vw;
                h2 {
                  font-size: 0.6vw;
                  margin: 10% 5% 0;
                }
                &_key {
                  margin-top: 2%;
                  display: inline-block;
                  span {
                    font-size: 0.8vw;
                    font-family: "yasasi b";
                  }
                }
                &_img {
                  width: 80%;
                  height: 28%;
                  position: relative;
                  margin: 2% auto 0;
                  &_left,
                  &_right {
                    position: absolute;
                    top: 50%;
                    transform: translateY(-50%);
                    font-size: 1.5vw;
                    font-family: "yasasi b";
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
                        height: 100%;
                        left: 10%;
                      }
                      &:nth-child(2) {
                        height: 50%;
                        right: 14%;
                      }
                    }
                  }
                  &_and {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    font-size: 0.8vw;
                    font-family: "yasasi b";
                    font-weight: 700;
                  }
                }
                &_h3 {
                  font-size: 0.5vw;
                  width: 100%;
                  margin: 0 5%;
                  line-height: 1.4;
                  font-family: "yasasi b";
                  margin-top: 3%;
                }
                &_descri {
                  margin-top: 1%;
                  margin: 2% 5% 0;
                  font-size: 0.5vw;
                  line-height: 1.4;
                  span {
                    &:nth-of-type(2) {
                      display: inline-block;
                    }
                  }
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
              .req {
                position: relative;
                z-index: 2;
                &_logo {
                  position: absolute;
                  height: 3vw;
                  width: 3vw;
                  right: 0.5vw;
                  top: 0.5vw;
                  border-radius: 0.5vw;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  img {
                    height: 80%;
                  }
                  &:after {
                    content: "";
                    position: absolute;
                    height: 80%;
                    width: 80%;
                    border: solid #fff 0.1vw;
                    border-radius: 0.3vw;
                  }
                }
                &_fm {
                  position: absolute;
                  z-index: 1;
                  font-size: 0.6vw;
                  bottom: 24%;
                  right: 0.7vw;
                  width: 75%;
                  font-family: "yasasi b";
                  &_now {
                    position: relative;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    align-items: center;
                    width: 100%;
                    height: 2.3vw;
                    padding: 0.1vw;
                    .head {
                      position: absolute;
                      z-index: 3;
                      height: 1.6vw;
                      width: 1.6vw;
                      text-align: center;
                      line-height: 1.6vw;
                      border-radius: 50%;
                      left: -0.8vw;
                      top: -0.5vw;
                      color: #fff;
                      font-family: "yasasi b";
                    }
                    &:after {
                      content: "";
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      height: calc(100% - 0.3vw);
                      width: calc(100% - 0.3vw);
                      transform: translate(-50%, -50%);
                      background: #fff;
                    }
                    p {
                      position: relative;
                      z-index: 3;
                      width: 100%;
                      text-align: center;
                      font-size: 0.6vw;
                      line-height: 1.1vw;
                      white-space: nowrap;
                      &:nth-of-type(1) {
                        font-size: 0.4vw;
                      }
                    }
                    .line {
                      width: 80%;
                      height: 4%;
                      z-index: 4;
                    }
                  }
                  &_future {
                    position: relative;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    align-items: center;
                    width: 100%;
                    height: 2.3vw;
                    padding: 0.1vw;
                    margin-top: 10%;
                    .head {
                      position: absolute;
                      z-index: 3;
                      height: 1.6vw;
                      width: 1.6vw;
                      text-align: center;
                      line-height: 1.6vw;
                      border-radius: 50%;
                      left: -0.8vw;
                      top: -0.5vw;
                      color: #fff;
                    }
                    &:after {
                      content: "";
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      height: calc(100% - 0.3vw);
                      width: calc(100% - 0.3vw);
                      transform: translate(-50%, -50%);
                      background: #fff;
                    }
                    p {
                      position: relative;
                      width: 100%;
                      text-align: center;
                      z-index: 3;
                      font-size: 0.6vw;
                      line-height: 1.1vw;
                      white-space: nowrap;
                      &:nth-of-type(1) {
                        font-size: 0.4vw;
                      }
                    }
                    .line {
                      width: 80%;
                      height: 4%;
                      z-index: 4;
                    }
                  }
                  &_img {
                    position: absolute;
                    right: 0.5vw;
                    bottom: 2%;
                    height: 15%;
                    img {
                      height: 100%;
                    }
                  }
                }
              }
              &.red {
                &::after {
                  background: url("../assets/img/bg/red.png") center center
                    repeat;
                }
              }
              &.orange {
                &::after {
                  background: url("../assets/img/bg/orange.png") center center
                    repeat;
                }
              }
              &.lightblue {
                &::after {
                  background: url("../assets/img/bg/lightblue.png") center
                    center repeat;
                }
              }
              &.blue {
                &::after {
                  background: url("../assets/img/bg/blue.png") center center
                    repeat;
                }
              }
              &.yellow {
                &::after {
                  background: url("../assets/img/bg/yellow.png") center center
                    repeat;
                }
              }
              &.yellowgreen {
                &::after {
                  background: url("../assets/img/bg/yellowgreen.png") center
                    center repeat;
                }
              }
              &.green {
                &::after {
                  background: url("../assets/img/bg/green.png") center center
                    repeat;
                }
              }
              &.violet {
                &::after {
                  background: url("../assets/img/bg/violet.png") center center
                    repeat;
                }
              }
              &.pink {
                &::after {
                  background: url("../assets/img/bg/pink.png") center center
                    repeat;
                }
              }
              &.pinkvio {
                &::after {
                  background: url("../assets/img/bg/pinkvio.png") center center
                    repeat;
                }
              }
              &.brown {
                &::after {
                  background: url("../assets/img/bg/brown.png") center center
                    repeat;
                }
              }
              &.black {
                &::after {
                  background: url("../assets/img/bg/brown.png") center center
                    repeat;
                }
              }
              &.rainbow {
                &::after {
                  background: url("../assets/img/bg/red.png") center center
                    repeat;
                }
              }
              &::after {
                content: "";
                position: absolute;
                height: 300%;
                width: 300%;
                top: -100%;
                left: -100%;
                background-size: 3vw !important;
                opacity: 0.5;
                transform: rotate(45deg);
                touch-action: none;
              }
            }
          }
        }
      }
      &_title {
        position: absolute;
        top: 1.5vw;
        left: 1.5vw;
        color: #cd8256;
        font-size: 3vw;
        font-family: "yasasi b";
        animation: bIn 0.6s ease-in 0.1s backwards;
      }
    }
  }
}
@keyframes r-360 {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
@keyframes bIn {
  from,
  60%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }

  60% {
    opacity: 1;
    transform: scale3d(1.03, 1.03, 1.03);
  }

  to {
    opacity: 1;
    transform: scale3d(1, 1, 1);
  }
}
@keyframes bOut {
  from,
  60%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 1;
    transform: scale3d(1, 1, 1);
  }

  60% {
    opacity: 1;
    transform: scale3d(1.03, 1.03, 1.03);
  }

  to {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
}
@keyframes bInD {
  from,
  60%,
  75%,
  90%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, -3000px, 0);
    transform: translate3d(0, -3000px, 0);
  }

  60% {
    opacity: 1;
    -webkit-transform: translate3d(0, 25px, 0);
    transform: translate3d(0, 25px, 0);
  }

  75% {
    -webkit-transform: translate3d(0, -10px, 0);
    transform: translate3d(0, -10px, 0);
  }

  90% {
    -webkit-transform: translate3d(0, 5px, 0);
    transform: translate3d(0, 5px, 0);
  }

  to {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }
}
@keyframes bOutD {
  20% {
    -webkit-transform: translate3d(0, 10px, 0);
    transform: translate3d(0, 10px, 0);
  }

  40%,
  45% {
    opacity: 1;
    -webkit-transform: translate3d(0, -20px, 0);
    transform: translate3d(0, -20px, 0);
  }

  to {
    opacity: 0;
    -webkit-transform: translate3d(0, 1000px, 0);
    transform: translate3d(0, 1000px, 0);
  }
}
.v-lazy-image {
  opacity: 0;
  transition: all 0.7s;
}
.v-lazy-image-loaded {
  opacity: 1;
}
.up-enter,
.up-leave-to {
  opacity: 0;
}
.up-enter-active {
  transition: opacity 0s 0.3s;
}
.up-leave-active {
  transition: opacity 0.3s 0.3s;
}
.up-enter-to,
.up-leave {
  opacity: 1;
}
.pop-enter {
  opacity: 0;
}
.pop-enter-active {
  transition: opacity 0s 0.3s;
}
.pop-enter-to {
  opacity: 1;
}
.pop-leave-active {
  animation: bOutD 0.6s ease 0.1s;
}
</style>
