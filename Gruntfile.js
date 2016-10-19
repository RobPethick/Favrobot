"use strict";

module.exports = function (grunt) {
    grunt.loadNpmTasks('grunt-exec');
    grunt.loadNpmTasks("grunt-contrib-watch");

    grunt.initConfig({
        exec: {
            unitTests: "python.exe -m unittest"
        },
        watch: {
            py: {
                files: "**/*.py",
                tasks: ["exec:unitTests"]
            }
        }
    });

    grunt.registerTask("default", [
        "watch:py"
    ]);
};
