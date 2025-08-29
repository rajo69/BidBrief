export default function HomePage() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-8">
      <h1 className="text-3xl font-bold">Welcome to BidBrief</h1>
      <p className="mt-4 text-lg text-center max-w-prose">
        This is the Next.js frontend for BidBrief.  The application is currently under
        construction.  Use the navigation sidebar (to be implemented) to upload tender
        packs, view compliance checklists, generate answer plans and drafts, and export
        your responses to Word.
      </p>
    </main>
  );
}