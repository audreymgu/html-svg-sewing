import fs from 'fs';
import path from 'path';
import { JSDOM } from 'jsdom';
import HtmlToSvg from '@tooooools/html-to-svg';

const htmlPath = path.resolve('test.html'); 
const htmlContent = fs.readFileSync(htmlPath, 'utf8');

const dom = new JSDOM(htmlContent);
const { document } = dom.window;

const renderer = new HtmlToSvg({
  debug: false,
  ignore: '.html-only, video', // CSS selector
  fonts: [
    { family: 'Roboto', url: './fonts/Roboto-Regular.otf' },
    { family: 'Roboto', url: './fonts/Roboto-Bold.otf', weight: '600' },
    { family: 'Roboto', url: './fonts/Roboto-Regular.otf', style: 'italic' }
  ]
});

await renderer.preload();

const options = {
  rasterizeNestedSVG: true, // Convert <svg> into <image>
  splitText: false // Force text fragments to be rendered letter by letter
};
const transform = async (from, to) => to;

const svg = await renderer.render(document.querySelector('main'), options, transform);

fs.writeFileSync('output.svg', svg.outerHTML, 'utf8');
console.log('SVG successfully generated and saved to output.svg!');

renderer.destroy();