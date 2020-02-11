<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}
html,
body {
  height: 100%;
  width: 100%;
}
input[type="text"] {
  padding: 0;
  border: none;
  border-radius: 0;
  outline: none;
  background: none;
  color: #494949;
}
select {
  outline: none;
  text-indent: 0.01px;
  text-overflow: "";
  background: none transparent;
  vertical-align: middle;
  font-size: inherit;
  color: inherit;
  -webkit-appearance: button;
  -moz-appearance: button;
  appearance: button;
  color: #494949;
}
select::-ms-expand {
  display: none;
}
select:-moz-focusring {
  color: transparent;
  text-shadow: 0 0 0 #828c9a;
}
button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  outline: none;
  padding: 0;
  appearance: none;
}
#app {
  height: 100%;
  width: 100%;
  font-family: "yasasi r";
  color: #494949;
}
</style>
