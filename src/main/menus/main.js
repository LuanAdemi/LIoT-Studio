const openAboutWindow = require('about-window').default;
const join = require('path').join;
module.exports = function(app) {
    return {
        label: 'Electron',
        submenu: [{
            label: 'Quit',
            accelerator: 'Command+Q',
            click: () => app.quit()
        },{
            label: 'About',
                click: () =>
                    openAboutWindow({
                        icon_path: join(__dirname, '512x512.png'),
                        copyright: '© 2018 LuanAdemi',
                        package_json_dir: __dirname,
                        license: 'MIT',
                        product_name: "LIoT Studio",
                        css_path: join(__dirname, 'style.css'),
                        homepage: "https://luanademi.github.io"
                    })
        
    
       
}]
}
}