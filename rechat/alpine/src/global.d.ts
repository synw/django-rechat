import { Alpine as AlpineType } from 'alpinejs';
import { htmx as HtmxType } from "htmx.org";
import { Instant as InstantType } from "djangoinstant";

declare global {
  var Alpine: AlpineType;
  var htmx: HtmxType;
  var Instant: InstantType;
}

