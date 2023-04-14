#!/usr/bin/node
/* Command line args in js is made using process.argv
 * process.argv is an array that contains all args of the CLI
 * process.argv[0] contains the abs path to the node binary file
 * process.argv[1] contains the abs file to the .js file in which the js
 * engine runs
 * so process.argv[2] contains users passed args
 */
if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
