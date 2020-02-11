<template>
  <div class="form" :class="[color, { fixed: post }]">
    <div class="form_bg">
      <h2 class="title">Melike</h2>
      <div class="input">
        <div class="form_img">
          <div class="form_img_left" :style="{ color: Color(color) }">
            {
          </div>
          <div class="form_img_icon">
            <v-lazy-image
              :src="i"
              alt=""
              v-for="i in Icons(color)"
              :key="i.id"
            />
          </div>
          <div class="form_img_and">&&</div>
          <div class="form_img_right" :style="{ color: Color(color) }">
            }
          </div>
        </div>
        <div class="form_descri">
          <p>
            <span>{{ Word(color) }}のようなあなた</span>
          </p>
        </div>
        <transition name="form" mode="out-in">
          <form @submit.prevent="postData" class="form_input" v-if="!post">
            <div class="form_input_in">
              <label for="job">
                あなたの職業は？
              </label>
              <input
                type="text"
                v-model="form.job"
                v-validate="'required|max:20'"
                data-vv-as="職業"
                name="job"
                placeholder="例:Webデザイナー/学生"
                :class="[
                  { input: form.job },
                  { 'has-error': errors.has('job') }
                ]"
              />
              <span class="att" v-if="errors.has('job')">!</span>
              <span class="war" v-if="errors.has('job')">{{
                errors.first("job")
              }}</span>
            </div>
            <div class="form_input_in">
              <label for="year">
                社会人何年目ですか？<br /><span class="sub"
                  >※学生は学年を入力</span
                >
              </label>
              <select
                v-model="form.year"
                name="year"
                data-vv-as="年数"
                :class="[
                  { input: form.year },
                  { 'has-error': errors.has('year') }
                ]"
                v-validate="'required'"
              >
                <option hidden disabled selected>-</option>
                <option :value="n" v-for="n of 20" :key="n">
                  {{ n }}
                </option>
              </select>
              <p>年</p>
              <span class="att select" v-if="errors.has('year')">!</span>
              <span class="war select" v-if="errors.has('year')">{{
                errors.first("year")
              }}</span>
            </div>
            <div class="form_input_in">
              <label for="now">
                今大切にしていることは？
              </label>
              <input
                type="text"
                v-model="form.now"
                v-validate="'required|max:6'"
                name="now"
                data-vv-as="大切にしてること"
                placeholder="例:学び"
                :class="[
                  { input: form.now },
                  { 'has-error': errors.has('now') }
                ]"
              />
              <span class="att" v-if="errors.has('now')">!</span>
              <span class="war" v-if="errors.has('now')">{{
                errors.first("now")
              }}</span>
            </div>
            <div class="form_input_in">
              <label for="future">
                未来大事にしたいことは？
              </label>
              <input
                type="text"
                v-model="form.future"
                v-validate="'required|max:6'"
                name="future"
                data-vv-as="未来大事にしいたいこと"
                placeholder="例:影響"
                :class="[
                  { input: form.future },
                  { 'has-error': errors.has('future') }
                ]"
              />
              <span class="att" v-if="errors.has('future')">!</span>
              <span class="war" v-if="errors.has('future')">{{
                errors.first("future")
              }}</span>
            </div>
            <div class="form_input_btn">
              <button :disabled="click">確認する</button>
            </div>
          </form>
          <div class="form_conf" v-else>
            <h3 class="form_conf_title">
              入力内容をご確認ください
            </h3>
            <div class="form_conf_list">
              <div class="form_conf_list_in">
                <h4 class="form_conf_list_in_title">あなたの職業は？</h4>
                <p>{{ form.job }}</p>
              </div>
              <div class="form_conf_list_in">
                <h4 class="form_conf_list_in_title">
                  社会人何年目ですか？<br /><span class="sub"
                    >※学生は学年を入力</span
                  >
                </h4>
                <p>{{ form.year }}年</p>
              </div>
              <div class="form_conf_list_in">
                <h4 class="form_conf_list_in_title">
                  今大切にしていることは？
                </h4>
                <p>{{ form.now }}</p>
              </div>
              <div class="form_conf_list_in">
                <h4 class="form_conf_list_in_title">
                  未来大事にしたいことは？
                </h4>
                <p>{{ form.future }}</p>
              </div>
              <div class="form_conf_list_btns">
                <div class="form_conf_list_btns_btn">
                  <button @click="toform" :disabled="!click">修正</button>
                </div>
                <div class="form_conf_list_btns_btn">
                  <!-- <button @click="sendPost">送信する</button> -->
                  <button @click="sendPost" :disabled="!click">送信する</button>
                </div>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </div>
    <div class="form_send" v-if="send">
      <div class="form_send_inner">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <div class="form_send_inner_bg">
          <div class="check">
            <div class="line"></div>
            <div class="line"></div>
          </div>
        </div>
        <p>送信完了</p>
      </div>
    </div>
  </div>
</template>

<script>
import * as firebase from "firebase/app";
import "firebase/database";
import smoothscroll from "smoothscroll-polyfill";
export default {
  data() {
    return {
      color: "no color",
      id: 0,
      form: {
        job: "",
        year: "",
        now: "",
        future: ""
      },
      post: false,
      click: false,
      send: false
    };
  },
  methods: {
    postData() {
      this.$validator.validateAll().then(res => {
        if (res) {
          this.post = true;
          setTimeout(() => {
            this.click = true;
          }, 700);
        } else {
          this.post = false;
        }
      });
    },
    rum() {
      return Math.random()
        .toString(32)
        .substring(2);
    },
    toform() {
      this.post = false;
      setTimeout(() => {
        this.click = false;
      }, 700);
    },
    sendPost() {
      if (this.post) {
        this.send = true;
        let r = this.rum();
        firebase
          .database()
          .ref("view")
          .push(
            {
              uniq: r,
              id: this.id,
              color: this.color,
              job: this.form.job,
              year: this.form.year,
              now: this.form.now,
              future: this.form.future
            },
            () => {
              setTimeout(() => {
                document.querySelector(".form_send").addEventListener(
                  "animationend",
                  function r(name) {
                    if (name.animationName == "s-t") {
                      document
                        .querySelector(".form_send")
                        .removeEventListener("animationend", r, false);
                      location.href =
                        "https://htandmy.github.io/evaluation_system/#/visitorsignin";
                    }
                  },
                  false
                );
              }, 100);
            }
          );
      } else {
        alert("不正な入力です");
        this.toform();
      }
    }
  },
  created() {
    this.post = false;
    this.click = false;
    this.send = false;
    if (this.$route.query.color && this.$route.query.id) {
      this.color = this.$route.query.color;
      this.id = this.$route.query.id;
    } else {
      this.$router.push("/error");
    }
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
    }
  },
  watch: {
    post: function() {
      smoothscroll.polyfill();
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    },
    send: function(n) {
      if (n) {
        document.querySelector("body").style.overflow = "hidden";
      } else {
        document.querySelector("body").style.overflow = "visible";
      }
    }
  }
};
</script>

<style lang="scss">
.form {
  position: relative;
  width: 100%;
  min-height: 100%;
  overflow: hidden;
  &_bg {
    width: 85%;
    overflow: hidden;
    margin: 30px auto;
    background: #fff;
    h2 {
      font-size: 27px;
      text-align: center;
      font-family: "yasasi b";
      margin-top: 2vw;
    }
  }
  &_img {
    position: relative;
    max-width: 270px;
    height: 56px;
    margin: 1vh auto 0;
    &_left,
    &_right {
      position: absolute;
      line-height: 56px;
      font-size: 48px;
      top: 0;
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
      position: relative;
      img {
        height: 90%;
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        &:nth-child(1) {
          left: 14%;
        }
        &:nth-child(2) {
          right: 14%;
        }
      }
    }
    &_and {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-size: 27px;
      font-family: "yasasi b";
      font-weight: 700;
    }
  }
  &_descri {
    width: 100%;
    text-align: center;
    margin-top: 2vw;
  }
  &_input {
    width: 95%;
    margin: 0 auto;
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    &_in {
      position: relative;
      width: 100%;
      margin-top: 10vw;
      display: flex;
      flex-wrap: wrap;
      label {
        font-size: 21px;
        font-family: "yasasi b";
        display: inline-block;
        width: 100%;
        .sub {
          font-size: 14px;
          font-family: "yasasi r";
          display: inline-block;
        }
      }
      p {
        line-height: 36px;
        margin-left: 10px;
      }
      input {
        border-bottom: 2px solid #cd8256;
        margin: 0 5px;
        width: 100%;
        height: 24px;
        padding: 5px;
        transition: all 0.2s ease-in;
        &:focus {
          border-color: #aac864;
        }
        &.has-error {
          border-color: #ff694b;
        }
      }
      select {
        width: 30%;
        padding: 5px;
        margin-left: 5px;
        border: 2px solid #cd8256;
        box-sizing: border-box;
        transition: all 0.2s ease-in;
        &:focus {
          border-color: #aac864;
        }
        &.has-error {
          border-color: #ff694b;
        }
      }
      p,
      input,
      select {
        font-size: 17px;
        margin-top: 2vw;
        &.input {
          border-color: #aac864;
        }
      }
      .att {
        position: absolute;
        bottom: 7px;
        right: 8px;
        height: 24px;
        width: 24px;
        line-height: 24px;
        background: #ff3c15;
        text-align: center;
        border-radius: 50%;
        color: #fff;
        font-family: "yasasi b";
        font-size: 17px;
        animation: bIn 0.4s ease-in both 0.1s;
        &.select {
          left: 42%;
        }
      }
      .war {
        position: absolute;
        top: 110%;
        left: 10px;
        font-size: 14px;
        color: #ff694b;
        animation: bIn 0.4s ease-in both 0.1s;
      }
    }
    &_btn {
      background: #aac864;
      height: 64px;
      width: 100%;
      margin: 13vw auto;
      text-align: center;
      border-radius: 5px;
      position: relative;
      button {
        font-size: 27px;
        font-family: "yasasi b";
        color: #fff;
        line-height: 64px;
        width: 100%;
      }
      &:after {
        content: "";
        position: absolute;
        height: calc(100% - 6px);
        width: calc(100% - 6px);
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        border: dashed 2px #fff;
        box-sizing: border-box;
        border-radius: 5px;
        pointer-events: none;
      }
    }
  }
  &_conf {
    width: 95%;
    margin: 30px auto;
    &_title {
      font-size: 17px;
      text-align: center;
      width: 100%;
    }
    &_list {
      width: 96%;
      margin: 30px auto;
      &_in {
        margin-top: 20px;
        padding-bottom: 5px;
        &_title {
          font-size: 21px;
          font-family: "yasasi b";
          .sub {
            font-size: 14px;
            font-family: "yasasi r";
          }
          span {
            display: inline-block;
          }
        }
        p {
          margin-top: 10px;
          font-size: 21px;
          height: 24px;
          padding: 5px;
        }
      }
      &_btns {
        height: 64px;
        width: 100%;
        margin: 40px auto 40px;
        text-align: center;

        display: grid;
        grid-gap: 10px;
        grid-template-columns: 1fr 2fr;
        &_btn {
          position: relative;
          border-radius: 5px;
          background: #aac864;
          &:nth-child(1) {
            background: #cd8256;
          }
          width: 100%;
          height: 100%;
          button {
            font-size: 27px;
            font-family: "yasasi b";
            color: #fff;
            line-height: 64px;
            width: 100%;
          }
          &:after {
            content: "";
            position: absolute;
            height: calc(100% - 6px);
            width: calc(100% - 6px);
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            border: dashed 2px #fff;
            box-sizing: border-box;
            border-radius: 5px;
            pointer-events: none;
          }
        }
      }
    }
  }
  &_send {
    position: fixed;
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
    &::after {
      content: "";
      position: absolute;
      height: 100%;
      width: 100%;
      top: 0;
      left: 0;
      background: #000;
      opacity: 0.3;
      z-index: 10;
    }
    &_inner {
      position: absolute;
      height: 60vw;
      width: 60vw;
      top: calc(50% - 30vw);
      left: calc(50% - 30vw);
      z-index: 999;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      animation: s-t 0.7s ease-in forwards 2.7s;
      &_bg {
        position: absolute;
        height: 90%;
        width: 90%;
        background: #aac864;
        animation: bIn 0.5s ease-in both 1s;
        border-radius: 10px;
        .check {
          position: relative;
          height: 40%;
          width: 40%;
          margin: -5% auto 0;
          overflow: hidden;
          transform: rotate(-45deg);
          .line {
            position: absolute;
            background: #fff;
            opacity: 0.7;
            &:nth-child(1) {
              height: 70%;
              width: 6px;
              top: 35%;
              animation: h-100 0.2s linear both 1.5s,
                o-1-7 0.4s ease-in forwards 1.9s;
            }
            &:nth-child(2) {
              height: 6px;
              width: 100%;
              left: 6px;
              bottom: 0;
              animation: w-100 0.2s ease-in both 1.7s,
                o-1-7 0.4s ease-in forwards 1.9s;
            }
          }
        }
        &::after {
          content: "";
          position: absolute;
          height: calc(100% - 16px);
          width: calc(100% - 16px);
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          border-radius: 5px;
          box-sizing: border-box;
          border: dashed 2px #fff;
        }
      }
      span {
        position: absolute;
        background: #aac864;
        &:nth-child(1) {
          top: 0;
          left: 0;
          height: 2px;
          width: 100%;
          animation: s-1 0.8s cubic-bezier(0.76, -0.01, 0.25, 1) both 0.2s;
        }
        &:nth-child(2) {
          bottom: 0;
          left: 0;
          height: 2px;
          width: 100%;
          animation: s-2 0.8s cubic-bezier(0.76, -0.01, 0.25, 1) both 0.2s;
        }
        &:nth-child(3) {
          top: 0;
          right: 0;
          height: 100%;
          width: 2px;
          animation: s-3 0.8s cubic-bezier(0.76, -0.01, 0.25, 1) both 0.2s;
        }
        &:nth-child(4) {
          bottom: 0;
          left: 0;
          height: 100%;
          width: 2px;
          animation: s-4 0.8s cubic-bezier(0.76, -0.01, 0.25, 1) both 0.2s;
        }
      }
      p {
        position: relative;
        color: #fff;
        margin-top: 50%;
        font-size: 27px;
        font-family: "yasasi b";
        animation: bIn 0.5s ease-in both 1.7s;
      }
    }
  }
}
.form {
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
      background: url("../assets/img/bg/yellowgreen.png") center center repeat;
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
    content: "";
    position: fixed;
    height: 300%;
    width: 300%;
    top: -100%;
    left: -100%;
    background-size: 50px;
    opacity: 0.5;
    transform: rotate(45deg);
    z-index: -1;
  }
  .form-enter-active {
    transition: all 0.3s ease-in 0.1s;
  }
  .form-leave-active {
    transition: all 0.3s ease-in;
  }
  .form-enter {
    opacity: 0;
  }
  .form-leave-active {
    opacity: 0;
  }
}
@keyframes o-1-7 {
  from {
    opacity: 0.7;
  }
  to {
    opacity: 1;
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
@keyframes fade {
  from {
    transform: translateY(150px);
  }
  to {
    transform: translate(0);
  }
}
@keyframes s-1 {
  from {
    transform: translateX(-100%);
  }
  50% {
    transform: translateX(0%);
  }
  to {
    transform: translateX(100%);
  }
}
@keyframes s-2 {
  from {
    transform: translateX(100%);
  }
  50% {
    transform: translateX(0%);
  }
  to {
    transform: translateX(-100%);
  }
}
@keyframes s-3 {
  from {
    transform: translateY(100%);
  }
  50% {
    transform: translateY(0%);
  }
  to {
    transform: translateY(-100%);
  }
}
@keyframes s-4 {
  from {
    transform: translateY(-100%);
  }
  50% {
    transform: translateY(0%);
  }
  to {
    transform: translateY(100%);
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
@keyframes w-100 {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}
@keyframes h-100 {
  from {
    height: 0;
  }
  to {
    height: 100%;
  }
}
@keyframes s-t {
  20% {
    transform: translate3d(0, -10px, 0);
  }

  40%,
  45% {
    opacity: 1;

    transform: translate3d(0, 20px, 0);
  }

  to {
    opacity: 0;

    transform: translate3d(0, -2000px, 0);
  }
}
</style>
