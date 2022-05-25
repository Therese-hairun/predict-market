import moment from "moment";

export const API_URL = process.env.VUE_APP_API_URL || "http://localhost:8000";
export const SHARE_URL = process.env.VUE_APP_SHARE_URL;
export const EMAIL = "contact@predictmarket.io";

export const SMS_CODE = Math.floor(100000 + Math.random() * 900000);
export const ERROR_COUNT = 4;
export const RESEND_WAITING = 60000;

export const PARAPHRASE = "hinc robur et securitas";

export function formatDate(dateFormat, item) {
  return moment(item).format(dateFormat);
}
