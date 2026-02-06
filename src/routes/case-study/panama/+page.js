// import { dev } from '$app/environment';

// // we don't need any JS on this page, though we'll load
// // it in dev so that we get hot module replacement
// export const csr = dev;

// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
import Papa from 'papaparse';

export async function load({ fetch }) {
    const contentFile = await fetch('/web-assets/case-study/panama/panama-content.csv');
    const contentText = await contentFile.text();

    const parsedContent = Papa.parse(contentText, {
        header: true,     
        encoding: "utf-8",
        skipEmptyLines: true
    });

    function groupByAnimation(arr) { // chop big animation csv into individual parts
        return arr.reduce((groups, item) => {
            const lastGroup = groups[groups.length - 1];

            if (!lastGroup || lastGroup.animation !== item.animation) {
                groups.push({ animation: item.animation, items: [item] });
            } else {
                lastGroup.items.push(item);
            }

            return groups;
        }, []);
    }

    const menuFile = await fetch('/web-assets/case-study/panama/panama-menuitems.csv');
    const menuText = await menuFile.text();

    const parsedMenu = Papa.parse(menuText, {
        header: true,     
        encoding: "utf-8",
        skipEmptyLines: true
    });

    return { animations: groupByAnimation(parsedContent.data), menuItems: parsedMenu.data };
}

export const prerender = true; 


