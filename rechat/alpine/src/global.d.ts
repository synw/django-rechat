import { Alpine as AlpineType } from 'alpinejs';
import { htmx as HtmxType } from "htmx.org";

declare global {
  var Alpine: AlpineType;
  var htmx: HtmxType;
}

