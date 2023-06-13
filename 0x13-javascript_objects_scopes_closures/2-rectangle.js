#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.widht = w;
      this.height = h;
    }
    return this.prototype;
  }
}

module.exports = Rectangle;
