var treeData = [{
    "name": "Niclas Superlongsurname",
    "class": "man",
    "textClass": "emphasis",
    "marriages": [{
      "spouse": {
        "name": "Iliana",
        "class": "woman"
      },
      "children": [{
        "name": "James",
        "class": "man",
        "marriages": [{
          "spouse": {
            "name": "Alexandra",
            "class": "woman"
          },
          "children": [{
            "name": "Eric",
            "class": "man",
            "marriages": [{
              "spouse": {
                "name": "Eva",
                "class": "woman"
              }
            }]
          }, {
            "name": "Jane",
            "class": "woman"
          }, {
            "name": "Jasper",
            "class": "man",
            "extra": {
              "favorite_color": "Blue"
            }
          }, {
            "name": "Emma",
            "class": "woman"
          }, {
            "name": "Julia",
            "class": "woman"
          }, {
            "name": "Jessica",
            "class": "woman"
          }]
        }]
      }]
    },
    {
        "spouse": {
          "name": "Iliana2",
          "class": "woman"
        },
        "children": [{
          "name": "James",
          "class": "man",
          "marriages": [{
            "spouse": {
              "name": "Alexandra",
              "class": "woman"
            },
            "children": [{
              "name": "Eric",
              "class": "man",
              "marriages": [{
                "spouse": {
                  "name": "Eva",
                  "class": "woman"
                }
              }]
            }, {
              "name": "Jane",
              "class": "woman"
            }, {
              "name": "Jasper",
              "class": "man",
              "extra": {
                "favorite_color": "Blue"
              }
            }, {
              "name": "Emma",
              "class": "woman"
            }, {
              "name": "Julia",
              "class": "woman"
            }, {
              "name": "Jessica",
              "class": "woman"
            }]
          }]
        }]
      }]
  }]

  var options ={
    target: '#graph',
    debug: false,
    width: 600,
    height: 600,
    hideMarriageNodes: true,
    marriageNodeSize: 10,
    callbacks: {
      /*
        Callbacks should only be overwritten on a need to basis.
        See the section about callbacks below.
      */
    },
    margin: {
      top: 0,
      right: 0,
      bottom: 0,
      left: 0
    },
    nodeWidth: 100,
    styles: {
      node: 'node',
      linage: 'linage',
      marriage: 'marriage',
      text: 'nodeText'
    }
  }