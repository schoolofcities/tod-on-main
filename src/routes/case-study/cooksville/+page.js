// import { dev } from '$app/environment';

// // we don't need any JS on this page, though we'll load
// // it in dev so that we get hot module replacement
// export const csr = dev;

// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
import Papa from 'papaparse';

export async function load({ fetch }) {
    //update fetch url to match correct file
    const res = await fetch('/web-assets/case-study/cooksville/cooksville-content.csv');
    const csvText = await res.text();

    const parsed = Papa.parse(csvText, {
        header: true,      // CSV has column names
        encoding: "utf-8",
        skipEmptyLines: true
    });

    return { rows: parsed.data };
}

// export const prerender = true;
