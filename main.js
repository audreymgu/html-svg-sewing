import HtmlToSvg from '@tooooools/html-to-svg'

// Instanciate a new renderer
const renderer = new HtmlToSvg({
  debug: false,
  ignore: '.html-only, video', // CSS selector
  fonts: [
    { family: 'Roboto', ur/fonts/Roboto-Regular.otf' },
    { family: 'Roboto', url: './fonts/Roboto-Bold.otf', weight: '600' },
    { family: 'Roboto', url: './fonts/Roboto-Regular.otf', style: 'italic' }
  ]
})

// Preload the fonts inside the renderer
await renderer.preload()
  
// Render a DOMElement
const options = { 
  rasterizeNestedSVG: true, // Convert <svg> into <image>
  splitText: false // Force text fragments to be renderered letter by letter
}

const transform = async (from, to) => to

const svg = await renderer.render(document.querySelector('main'), options, transform)

// Do whatever you want with the returned shadow SVGElement
document.body.appendChild(svg)
download(svg.outerHTML)

renderer.destroy()