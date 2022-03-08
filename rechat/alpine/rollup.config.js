import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import typescript from '@rollup/plugin-typescript';
import { terser } from 'rollup-plugin-terser';

const isProduction = !process.env.ROLLUP_WATCH;

export default {
  input: 'src/main.ts',
  output: {
    file: '../static/rechat/index.js',
    format: 'iife',
    name: '$alpine',
  },
  plugins: [
    typescript(),
    resolve({
      jsnext: true,
      main: true,
      browser: true,
    }),
    commonjs(),
    isProduction && terser(),
  ],
};
